### Sentence Query - Coding Interview Problem

'''
In this, array of sentences will be given and also a array of phrases. You must determine which sentences contain ALL of the word phrases.

Input:
3
jim likes mary
kate likes tom
tom does not like jim
2
jim tom
likes

Ouput:
2
0 1

Note - 2 has been output since jim tom is contained in the sentence of the index 2.
likes is there in the 0 and 1 indexed sentences.
'''

#solution
def query_sentence_match(query, sentence_dict):
    len_query = len(query.split())
    res_val = []
    for key, val in sentence_dict.items():
        FLAG_COUNTER = 0
        for i in query.split():
            if i in val:
                FLAG_COUNTER+=1
            else:
                continue
        if FLAG_COUNTER==len_query:
            res_val.append(True)
        else:
            res_val.append(False)
    res = list(filter(lambda i: res_val[i], range(len(res_val))))
    return res

def main():
    n_sentences = int(input())
    sentences = []

    for i_sentences in range(0,n_sentences):
        tmp_sent = input()
        sentences[i_sentences]=tmp_sent
    n_queries = int(input())
    queries = []

    for j in range(0,n_queries):
        tmp_queries = input()
        queries.append(tmp_queries)

    # dict_check = {0: 'jim likes mary', 1:'kate likes tom', 2:'tom does not like jim'} #Sentence example for test
    # query = ['jim tom', 'likes'] #Phrase example for test

    for i_query in queries:
        res = query_sentence_match(i_query, sentences)
        print(*res)

if __name__ == "__main__":
    main()
