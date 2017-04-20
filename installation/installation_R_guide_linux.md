# Linux Installation Guide 

1. Download and install miniconda (please be careful to choose the right installer which suits your system architecture) - [http://conda.pydata.org/miniconda.html](http://conda.pydata.org/miniconda.html)

2. From the command prompt install `r-essentials` via the `r` channel

        conda install -c r r-essentials

3. From command prompt run `R`

4. In the R shell that has opened, run the command

        install.packages('rvest',repos = "http://ftp.iitm.ac.in/cran")

5. Navigate to the repository for Introduction to Data Science in R and run 

        jupyter notebook

**You should be able to create R notebooks from Jupyter now.**
