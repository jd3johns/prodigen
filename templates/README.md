# Introduction

This README was created on $DATE by Luke Johnston for project
${ProjectDir}.

This README details how this research directory is structured, how
files should be run, what the different files do, and what to do if
the directory is outside of Luke's computer system.

If the files within this project are going to be run, the prerequisite
programs are: make (GNU make), \LaTeX\ (\TeX Live or Mik\TeX, etc.;
also will likely need pgfplotstable from \LaTeX; for the .tex files),
pandoc (for the markdown (.md) conversion), shell script (e.g. bash),
SAS, R, knitr (for R), and git (version control).  To open up some
programs, Inkscape (.svg files), Dia (.dia files), Docear/Freeplane
(.mm files) and TETRAD (the files in the `dag` folder) will also need
to be installed.

# Directory structure and explanation

The project directory is generally structured with `dataset`,
`scripts`, `output`, `lit`, and `report` folders, as well as a version
control `.git` folder.  As a caveat, there may be folders other than
the below that were created for an ad hoc purpose.

## `dataset` folder:

The `dataset` folder contains the dataset (both the original and the
project subsetted dataset), all of which are write-locked to prevent
accidental changes to the data.  If the dataset is within its original
file structure (i.e. the original dataset is located on the operating
system), then just `cd` to the parent directory (main project folder)
and type `make refresh` in the terminal to update the dataset.
Otherwise, the dataset remains as it was since its last update.

## `lit` folder

The `lit` folder contains files relevant to the literature and for
understanding the causal pathways.  There are three folders within the
parent `lit` folder:

* `mindmap` --- Contains mindmaps that are used to help organize the
  articles that were read, the information and findings from the
  articles, and to help structure writing up the report.
* `diagrams` --- Contains conceptual diagrams to better understand the
  biology underlying the research question and to understand the
  findings of the literature.
	  * `dag` --- Contains directed acyclic graphs (DAG) to represent
         the underlying causal and confounding pathways.  DAGs are
         used to help guide which covariates to include when building
         predictive models that test the relationship between the
         exposure and the outcome.
* `bib-db` --- After the manuscript has been accepted and submitted to
  a journal, the .aux file generated by \LaTeX\ (in the `report/tmp`
  folder) can be used to subset the master .bib file into only those
  references used.  This subsetted .bib file should be copied into
  this folder for future reference and to maintain the modular nature
  of each research project folder.

## `scripts` folder

The `scripts` folder contains the scripts which runs the analyses and
figure generations, outputting them into the output folder.  There are
various .sas and .R files that achieve different purposes, for
example, the `variables.sas` file subsets the original dataset and
creates relevant variables while the `analysis.sas` file will run the
analyses and output the results that can also be used in the
generation of the report.  This folder also contains another folder:

* `functions` --- Contains the files that have all the needed
  functions, macros, and formats for the script files in the scripts
  folder.  These files are read-only.  If they need to be updated,
  type `make refresh` into the terminal in the parent directory (Note:
  this will not work if the original files are not present on the
  system).

## `output` folder

output folder (with the internal figs folder) will contain all the
output files generated from the SAS and R scripts which are necessary
for the analysis and the report.  The idea behind the output folder is
that you should be able to delete all the files, run the scripts
again, and generate all the necessary result files.  In fact, in the
parent directory of the project folder (i.e. ./), the command `make
clean` should be run in the terminal to delete all output files to
make sure that the script files are generating all the needed output
files.  This folder also contains the `figs` folder to store all the
figures generated by R.

## `report` folder

The `report` folder contains the files to create the final report for
the research project.  The hope is that all the results within the
report can be reproducible and replicable easily (using knitr and
pgfplotstable) so that if the analysis changes, all numbers change
automagically as well.  This process is known as "reproducible
research" and should be actively adhered to, to be as scientifically
responsible and rigorous as possible.  In order to generate the
document, type the command `cd ./report`, followed by `make` into the
terminal to generate the document in pdf format.  Changes to the
report that require another `make` run do not need to `cd` again.  To
create a Word/OpenDocument final report, first the package "tex4ht" in
the ${ProjectDir}ManuscriptMain.tex file must be uncommented, then
simply type `make doc` into the terminal.
