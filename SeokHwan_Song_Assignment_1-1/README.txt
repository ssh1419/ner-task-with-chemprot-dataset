COM S 661
Assignemnt 1
Read Me
SeokHwan Song




1. Version
   1. Python 3.7.4
   2. Pandas 0.25.1
   3. Numpy 1.17.2
   4. Spacy 2.3.2
   5. Nltk 3.4




2. Steps
   1. Please put this python file with the file of the assignment dataset in the same directory and compile it
   2. I used Jupyter notebook.
   3. You should install libraries above and pre-existing model called en_core_web_sm
      1. python -m spacy download en_core_web_sm
      2. You should put this command on terminal
   4. After that, you can follow the order before modeling
      1. If you want to model with blank Spacy model
         1. Run ‘#Train model with blank Spacy model’ and jump to ‘# New labels’
      2. If you want to model with # Train Model with pre-existing spacy model’ and jump to ‘# New labels’
   5. At the bottom of the code, you will get the scores (precision and f values)




3. Parameters
   1. I changed the size of the batch in ‘# Begin training by disabling other pipeline components’ 
      1. sizes = compounding().
      2.  [(1.0, 4.0, 1.001), (1., 10., 1.5), (4.0, 32.0, 1.001)]
   2. I changed the number of iterations in ‘# Begin training by disabling other pipeline components’
      1. for itn in range(30)
      2. 20, 30, 45