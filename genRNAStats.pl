#!/usr/bin/perl -w -I/home/stanley/ViennaRNA-1.5/Perl/blib/arch -I/home/stanley/ViennaRNA-1.5/Perl/blib/lib
############################################################################
# AUTHOR:  	Stanley NG Kwang Loong, stanley@bii.a-star.edu.sg
# DATE:		31/07/2005
# DESCRIPTION: Generates stats from fasta
############################################################################
use warnings;
use strict;
use Getopt::Long;
use RNA;

############################################################################
# Global Parameters and initialization if any.
############################################################################
chdir('./data/') or die "$!";
my $inFile="&STDIN";
my $outFile="&STDOUT";

#Define the monomers and dimers
my %gl_monomers = ('A' => 0,'C' => 0, 'G' => 0, 'U' => 0);
my %gl_dimers = ('AA' => 0, 'AC' => 0, 'AG' => 0, 'AU' => 0,
                 'CA' => 0, 'CC' => 0, 'CG' => 0, 'CU' => 0,
                 'GA' => 0, 'GC' => 0, 'GG' => 0, 'GU' => 0,
                 'UA' => 0, 'UC' => 0, 'UG' => 0, 'UU' => 0);
my %gl_trimers = ('UUU' => 0, 'UUC' => 0, 'UUA' => 0, 'UUG' => 0, 'UCU' => 0, 'UCC' => 0, 'UCA' => 0, 'UCG' => 0, 'UAU' => 0, 'UAC' => 0, 'UAA' => 0, 'UAG' => 0, 'UGU' => 0, 'UGC' => 0, 'UGA' => 0, 'UGG' => 0, 'CUU' => 0, 'CUC' => 0, 'CUA' => 0, 'CUG' => 0, 'CCU' => 0, 'CCC' => 0, 'CCA' => 0, 'CCG' => 0, 'CAU' => 0, 'CAC' => 0, 'CAA' => 0, 'CAG' => 0, 'CGU' => 0, 'CGC' => 0, 'CGA' => 0, 'CGG' => 0, 'AUU' => 0, 'AUC' => 0, 'AUA' => 0, 'AUG' => 0, 'ACU' => 0, 'ACC' => 0, 'ACA' => 0, 'ACG' => 0, 'AAU' => 0, 'AAC' => 0, 'AAA' => 0, 'AAG' => 0, 'AGU' => 0, 'AGC' => 0, 'AGA' => 0, 'AGG' => 0,'GUU' => 0, 'GUC' => 0, 'GUA' => 0, 'GUG' => 0, 'GCU' => 0, 'GCC' => 0, 'GCA' => 0, 'GCG' => 0, 'GAU' => 0, 'GAC' => 0, 'GAA' => 0, 'GAG' => 0, 'GGU' => 0, 'GGC' => 0, 'GGA' => 0, 'GGG' => 0);

my $numseqs = 0;

############################################################################
# File IO
# Parse the command line.
############################################################################
Getopt::Long::Configure ('bundling');
GetOptions (
	'i|input_file=s' => \$inFile, 
	'o|output_file=s' => \$outFile
);

if(scalar(@ARGV) == 1 || !defined($inFile) || !defined($outFile)) { 
	die ("USAGE: $0 -i <input file> -o <output file>\n");
}

open (INFILE, "<$inFile") or die( "Cannot open input file $inFile: $!" );
open (OUTFILE, ">$outFile") or die ("Cannot open output file $outFile: $!");

# ID Len A C G U G+C A+U AA AC AG AU CA CC CG CU GA GC GG GU UA UC UG UU %A %C %G %U %G+C %A+U %AA %AC %AG %AU %CA %CC %CG %CU %GA %GC %GG %GU %UA %UC %UG %UU bp %bp mfe Nmfe Q D Subopt_size  
print (OUTFILE "ID\tLen\t");
#print (OUTFILE map { "$_\t" } (sort keys(%gl_monomers)));
#print (OUTFILE "G\+C\tA\+U\t");
#print (OUTFILE map { "$_\t" } (sort keys(%gl_dimers)));
print (OUTFILE map { "\%$_\t" } (sort keys(%gl_monomers)));
print (OUTFILE "\%G\+C\t\%A\+U\t");
print (OUTFILE map { "\%$_\t" } (sort keys(%gl_dimers)));
#print (OUTFILE map { "$_\t" } (sort keys(%gl_trimers)));
print (OUTFILE map { "\%$_\t" } (sort keys(%gl_trimers)));

print (OUTFILE "Npb\t");
print (OUTFILE "Nmfe\t");
print (OUTFILE "NQ\t");
print (OUTFILE "ND\t");

$| = 1;
# Read line by line.
while (my $line = uc(<INFILE>)) 
{

	chomp($line);
	
	
    if ($line =~ m/^>/)
    		{
    		 my $ID = substr($line, 1);
    		 print(OUTFILE "\n$ID\t");
    		}
    
    # Fasta Second Line i.e. RNA sequence
    elsif ($line =~ m/^[AaCcUuGgTt]/) {
    		$line =~ s/T/U/g;	    

		#Absolute Values
		my %aw_monomers = %gl_monomers;
		my %aw_dimers = %gl_dimers;
		my %aw_trimers = %gl_trimers;		

		$numseqs++;

		#remove white space etc
		$line =~ s/[^AaCcUuGg]//g;

		my $seqLen = length($line);
		print(OUTFILE "$seqLen\t");
		
		#compute monomer and dimer distribution
		for my $i (0..$seqLen-1) {		
			my $monomer = substr($line, $i, 1);
			$aw_monomers{$monomer}++ if defined $aw_monomers{$monomer};

			my $dimer = substr($line, $i, 2);
			$aw_dimers{$dimer}++ if defined $aw_dimers{$dimer};	
			
			my $trimer = substr($line, $i, 3);
			$aw_trimers{$trimer}++ if defined $aw_trimers{$trimer};		
		}	
		


		my $GC = $aw_monomers{'G'} + $aw_monomers{'C'};
		my $AU = $aw_monomers{'A'} + $aw_monomers{'U'};		

		

		
		#Print Percentage Values
		foreach my $monomer (sort (keys(%aw_monomers))){
			printf(OUTFILE "%.2f\t", $aw_monomers{$monomer}/$seqLen*100);
		}

		printf(OUTFILE "%.2f\t%.2f\t", $GC/$seqLen*100, $AU/$seqLen*100);
		

		foreach my $dimer (sort (keys(%aw_dimers))){
			printf(OUTFILE "%.2f\t", $aw_dimers{$dimer}/($seqLen-1)*100);
		}
		
		foreach my $trimer (sort (keys(%aw_trimers))){
			printf(OUTFILE "%.2f\t", $aw_trimers{$trimer}/($seqLen-2)*100);
		}
		
		my ($bp, $mfe, $Q, $D, $SS) = rnaAnalysis($line);
		printf(OUTFILE "%.4f\t", $bp/$seqLen);
		printf(OUTFILE "%.4f\t", $mfe/$seqLen);
		printf(OUTFILE "%.4f\t", $Q/$seqLen);
		printf(OUTFILE "%.4f\t", $D/$seqLen);

    }
	
    else { }
  
}#end of while loop

print (OUTFILE "\n");
close (INFILE) or die( "Cannot close input file $inFile: $!" );
close (OUTFILE) or die( "Cannot close output file $outFile: $!");
exit;

sub rnaAnalysis {
	my ($seq) = shift;
	my ($seqLen, $struct, $mfe) = (length($seq), RNA::fold($seq)); 
	my $bp = $struct =~ tr/(//; 
	my $Q = 0;
	my $D = 0;
		
	$RNA::pf_scale = exp((-1)*1.2*$mfe/(0.6163207755*$seqLen)) if ($seqLen > 1000); 

	# compute partition function and pair pobabilities matrix
	RNA::pf_fold($seq);   				
	# compute sum-of-entropy and bp-distance
	foreach my $j (1..$seqLen-1) {
		foreach my $k ($j+1..$seqLen) {
			my $p = RNA::get_pr($j, $k); # points to the computed pair probabilities
			if ($p > 0) {
				$Q += (-1)*$p*(log($p)/log(2));
				$D += $p*(1 - $p);
			}
		}
	}
	
	return ($bp, $mfe, $Q, $D, 0);
}
