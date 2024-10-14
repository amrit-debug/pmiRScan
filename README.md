[![Python 3.x](https://img.shields.io/badge/Python-3.X-green.svg)](https://www.python.org/)
[![pmiRScan]((http://www.csb.iitkgp.ac.in/applications/pmiRScan/index.php).
pmiRScan uses Light Gradient Boosting algorithm to classify and predict a sequences as pre-miRNAs or non-premiRNAs using combination of sequence and structural features. The secondary structures are calculated using RNAfold in Vienna2.5.1 package.

# Contents
- [Contents](#contents)
- [Requirements and installment](#requirements-and-installment)
- [Basic usage](#basic-usage)
- [Study demo](#study-demo)


# Requirements and installment
This software is developed with Python 3.X, Python 3.X is required as runtime environment.
- [Vienna 2.x.x](https://www.tbi.univie.ac.at/RNA/)

```shell
git clone https://github.com/amrit-debug/pmiRScan
cd pmiRScan
# virtual environment are recommended
python3 -m venv "/path/to/venv" (or conda environment)
pip install -r requirements.txt
```
# Basic usage
Users can use pmiRScan to classify and predict pre-miRNA sequences.

```usage:
python3 pmiRScan.py <input.fasta> <output>
```
# Study demo
Users can submit only RNA sequences in FASTA format as input and must provide an output file name:

The input file must be present in "/path/to/pmiRScan/data".

```shell
python3 pmiRScan.py input.fasta outfile

```
1. The secondary structure notation file will be generated as "/path/to/pmiRScan/out.txt"

2. All other output files including the outfile containing the predictions will be present in 
"/path/to/pmiRScan/results"

