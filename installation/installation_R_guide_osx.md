# Mac installation Guide for Introduction to Data Science in R

1. Download and install brew from - [http://brew.sh/](http://brew.sh/) 

2. Install r 
 
        brew install r

3. Install zeromq 
 
        brew install zeromq

4. Download and install miniconda2  from [here](http://conda.pydata.org/miniconda.html)

5. Install jupyter 

        conda install jupyter

6. From command prompt run `R`

7. In the R shell that has opened run the command

        install.packages(c('rzmq','repr','IRkernel','IRdisplay'),repos = c('http://irkernel.github.io/', getOption('repos')))

8. On successful completion of the previous command, in the R shell itself, make `IRKernel` available to jupyter by running the following command

        IRkernel::installspec(user = FALSE)

9. Navigate to the repository for Introduction to Data Science in R and run 

        jupyter notebook

**You should be able to create R notebooks from Jupyter now.**
