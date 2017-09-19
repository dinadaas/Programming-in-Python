
def uniform(domain):
    """Return a uniform distribution over the given domain"""
    return dict((v,1.0/len(domain)) for v in domain)

def valid_probability_distribution(p):
    if any(v<0 for v in p.values()): return False
    if(abs(sum(p.values())-1.0) > 1e-5): return False
    return True

def learn_discrete(dataset,virtual_count=1,domain=None):
    """Given a list of values in dataset, learns a discrete distribution
    over the value."""
    if(domain==None):
        domain = set(dataset)
    #TODO: generate a distribution over the domain from the data and
    dist = dict()
    for x in domain:
        value in dist.set(virtual_count)
    for i in dataset:
        dist[i] = dist[i]+1
    total = 0.0
    for key, val in dist.iteritems():
        dist[key] = dist[key]/total
    print dist
    return dist
    #taking into account the virtual counts
    #???return uniform(domain)

def learn_naive_bayes(class_key,feature_keys,
                      dataset,
                      class_prior_count=1,feature_posterior_count=1,
                      class_domain=None,feature_domains=None):
    """Estimating a Naive Bayes model from data.  Given a list of instances,
    learns a class prior P(C) and feature posteriors P(F1|C),...,P(Fk|C).
    Returns a pair (PC,PF) where PF is a dictionary mapping feature names
    to a conditional distributions.  Like in problem 1, a conditional
    distribution p gives P(F=f|C=f) in a table p[c_value][f_value].
    
    The prior counts are "virtual counts" for each value in the class's domain
    and the features' domains.
    """
    if class_domain == None:
        #compute the set of values that the class can take on
        class_domain = set([instance[class_key] for instance in dataset])
    if feature_domains == None:
        #compute the set of values that the features can take on
        feature_domains = dict()
    for f in feature_keys:
        if f not in feature_domains:
            feature_domains[f] = set([instance[f] for instance in dataset])

    #TODO: replace these lines with your work
    #create a uniform class prior
    PCuniform = uniform(class_domain)
    PFuniform = dict()
    #create uniform feature priors
    for f in feature_keys:
        PFf = dict()
        #for all values v in the class domain, PFf[v] is a distribution over f's
        #domain
        for class_v in class_domain:
            PFf[class_v] = uniform(feature_domains[f])
        PFuniform[f] = PFf

    

    #Hint: this will help you get started.
    #If you implement the learn_discrete function, this line learns the class prior
    PClearned = learn_discrete([instance[class_key] for instance in dataset],
                               class_prior_count,
                               class_domain)
    PFlearned = dict()
    #TODO what here?
    for feat in feature_keys:
        PFlearned[feat] = dict()
        for cd in class_domain:
            list = []
            for dat in dataset:
                if dat[class_key] == cd:
                    list.append(dat[feat])
            PFlearned[feat][cd] = learn_discrete(list, feature_posterior_count, feature_domains[feat])


    
    return (PClearned,PFlearned)

def p2():
    labeled_instances = [
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':0},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':0,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':0,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':0,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Not-Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Spam','f1':1,'f2':0,'f3':0,'f4':0},
        {'Label':'Spam','f1':1,'f2':1,'f3':1,'f4':1},
        {'Label':'Spam','f1':1,'f2':1,'f3':1,'f4':0},
        {'Label':'Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Spam','f1':0,'f2':1,'f3':0,'f4':1},
        {'Label':'Spam','f1':1,'f2':0,'f3':1,'f4':1},
        {'Label':'Spam','f1':1,'f2':0,'f3':1,'f4':1},
        {'Label':'Spam','f1':1,'f2':0,'f3':1,'f4':1},
        ]
    (PC,PF) = learn_naive_bayes('Label',['f1','f2','f3','f4'],
                                labeled_instances)
    print "Spam prior:",PC["Spam"]
    for f,PFf in PF.iteritems():
        print PFf
        print f," given Spam:",PFf["Spam"][1]
        print f," given Not-Spam:",PFf["Not-Spam"][1]
        
    assert(valid_probability_distribution(PC)),"Class prior is invalid"
    for f,PFf in PF.iteritems():
        assert(valid_probability_distribution(PFf["Spam"])),"Feature "+f+" given Spam is invalid"
        assert(valid_probability_distribution(PFf["Not-Spam"])),"Feature "+f+" given Not-Spam is invalid"

if __name__=="__main__":
    p2()
    
