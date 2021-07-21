from TILDE import TILDE

def classify():
    """shows an example of classification

       this is data about men,women and dogs
       h(man) means man is happy
       o(man,dog) means man owns dog
       r(man,woman,term) means man is in relationship with woman for long term or short term

    """

    tree = TILDE()
    
    '''
    print ("""shows an example of classification

           this is data about men,women and dogs
           h(man) means man is happy
           o(man,dog) means man owns dog
           r(man,woman,term) means man is in relationship with woman for long term or short term

           """)

    print ("\nlearning classification tree for man's happiness")

    #inputs to classification: data,examples,target and background
    train_data = ['o(m1,d1)','r(m1,w1,st)','o(m2,d2)','r(m2,w2,st)','o(m3,d3)','r(m3,w3,st)','o(m4,d4)','r(m4,w4,lt)','r(m5,w5,st)','r(m6,w6,lt)','r(m7,w7,lt)']
    train_pos = ['h(m1)','h(m2)','h(m4)','h(m6)']
    train_neg = ['h(m3)','h(m5)','h(m7)']
    target = 'h'
    bk = ['h(+man)','o(+man,-dog)','r(+man,-woman,#term)']

    #learns tree, can see tree clauses by printing tree.clauses
    tree.learn(train_data,bk,target,pos=train_pos,neg=train_neg)
    print ("\nlearned ordered tree clauses are:\n")
    print (tree.clauses)

    #inputs to testing
    test_data = train_data #cheating but you can add your own data
    test_example = train_pos[0] #just picking one example to show how it works
    infered_value = tree.infer(test_data,test_example)
    '''

    train_data = ['edgepiece(wh,or)','edgepiece(wh,re)','edgepiece(wh,gr)','edgepiece(wh,bl)',
                'edgepiece(ye,or)','edgepiece(ye,re)','edgepiece(ye,gr)','edgepiece(ye,bl)',
                'edge_center1(ye,re,ye)','edge_center2(ye,re,re)',
                'edge_center1(ye,gr,ye)','edge_center2(ye,gr,gr)',
                'edge_center1(ye,bl,re)','edge_center2(ye,bl,gr)',
                'edge_center1(ye,or,wh)','edge_center2(ye,or,re)',
                'edge_center1(wh,re,or)','edge_center2(wh,re,gr)',
                'edge_center1(wh,gr,re)','edge_center2(wh,gr,gr)',
                'edge_center1(wh,or,wh)','edge_center2(wh,or,ye)',
                'edge_center1(wh,bl,ye)','edge_center2(wh,bl,re)',
                'opposite(wh,ye)','opposite(bl,gr)','opposite(or,re)','opposite(ye,wh)',
                'opposite(gr,bl)','opposite(re,or)',
                'adjacent(wh,bl)','adjacent(wh,or)','adjacent(wh,re)','adjacent(wh,gr)',
                'adjacent(bl,re)','adjacent(bl,or)','adjacent(gr,re)','adjacent(gr,or)',
                'adjacent(ye,bl)','adjacent(ye,or)','adjacent(ye,re)','adjacent(ye,gr)',
                'adjacent(bl,wh)','adjacent(or,wh)','adjacent(re,wh)','adjacent(gr,wh)',
                'adjacent(re,bl)','adjacent(or,bl)','adjacent(re,gr)','adjacent(or,gr)',
                'adjacent(bl,ye)','adjacent(or,ye)','adjacent(re,ye)','adjacent(gr,ye)',
                'left_inplace(wh,or)','left_inplace(ye,re)','left_inplace(ye,gr)',
                'edge_inplace(ye,re)','edge_inplace(ye,gr)',
                'right_inplace(wh,gr)','right_inplace(ye,re)','right_inplace(ye,gr)',
                'move_left_one(ye,bl)','move_left_one(wh,re)','move_left_one(wh,gr)',
                'move_left_two(ye,or)','move_left_two(wh,bl)']
    train_pos = ['move_right_one(wh,re)','move_right_one(wh,or)','move_right_one(wh,bl)']
    train_neg = ['move_right_one(ye,bl)','move_right_one(wh,gr)',
                'move_right_one(ye,or)','move_right_one(ye,gr)','move_right_one(ye,re)']
    target = 'move_right_one'
    bk = ['move_right_one(+piece1,+piece2)', 'edge_center2(+piece1,+piece2,-piece)','adjacent(+piece2,+piece)']

    tree.learn(train_data,bk,target,pos=train_pos,neg=train_neg)
    print ("\nlearned ordered tree clauses are:\n")
    print (tree.clauses)

def regress():
    """shows an example of regression

       value for positive assumed 1 and negative -1 to demo regression

       this is data about men,women and dogs
       h(man) means man is happy
       o(man,dog) means man owns dog
       r(man,woman,term) means man is in relationship with woman for term length

    """
    
    print ("""shows an example of regression

           value for positive assumed 1 and negative -1 to demo regression

           this is data about men,women and dogs
           h(man) means man is happy
           o(man,dog) means man owns dog
           r(man,woman,term) means man is in relationship with woman long term or short term

          """)

    print ("\nlearning regression tree for man's happiness")

    tree = TILDE(typ="regression",score="WV")

    #inputs to classification: data,examples,target and background
    train_data = ['o(m1,d1)','r(m1,w1,st)','o(m2,d2)','r(m2,w2,st)','o(m3,d3)','r(m3,w3,st)','o(m4,d4)','r(m4,w4,lt)','r(m5,w5,st)','r(m6,w6,lt)','r(m7,w7,lt)']
    train_pos = ['h(m1)','h(m2)','h(m4)','h(m6)']
    train_neg = ['h(m3)','h(m5)','h(m7)']
    examples = {}

    #put value 1 for positive for demo purposes
    for ex in train_pos:
        examples[ex] = 1

    #put value -1 for negative
    for ex in train_neg:
        examples[ex] = -1
    
    target = 'h'
    bk = ['h(+man)','o(+man,-dog)','r(+man,-woman,#term)']

    #learns tree, can see tree clauses by printing tree.clauses
    tree.learn(train_data,bk,target,examples = examples)

    print ("\nlearned ordered tree clauses are:\n")
    print (tree.clauses)

    #inputs to testing
    test_data = train_data #cheating but you can add your own data
    test_example = train_pos[0] #just picking one example to show how it works

    infered_value = tree.infer(test_data,test_example)
    

if __name__ == '__main__':

    classify()
    #print ("="*80)
    #regress()
    
               
