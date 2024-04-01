from nltk.collocations import TrigramCollocationFinder # Word Prediction Module
from nltk.tokenize import word_tokenize  # Word Tokenize Module
import pandas as pd 

def prd(text):
        new_text = text

        def file_read():  # File Read and Store in Variable
            q = open("all_data.txt","r")
            data = q.read()
            q.close()
            return data


        data_txt = file_read()

        # Word Prediction
        first,second,third,count = [],[],[],[]
        f = TrigramCollocationFinder.from_words(word_tokenize(data_txt))
        for i in f.ngram_fd.items():
            try :
                first.append(i[0][0])
                second.append(i[0][1])
                third.append(i[0][2])
                count.append(i[1])
            except :
                pass

        # Make dataset
        dataset = pd.DataFrame({"First":first,"Second":second,"Third":third,"Count":count})
        dataset = dataset.sort_values(by="Count",ascending=False)

        index_no = dataset[dataset['First'] == new_text]

        if index_no.shape[0] > 1:
            first_word = index_no["Second"][index_no["Second"].index[0]]
            second_word = index_no["Second"][index_no["Second"].index[1]]
            third_word =  index_no["Third"][index_no["Third"].index[0]]
            return (first_word, second_word, third_word)
        elif index_no.shape[0] == 1:
            first_word = index_no["Second"][index_no["Second"].index[0]]
            second_word = new_text
            third_word =  index_no["Third"][index_no["Third"].index[0]]
            return (first_word, second_word, third_word)
        elif index_no.shape[0] == 0:
            first_word , second_word, third_word = new_text,new_text,new_text
            return (first_word, second_word, third_word)

