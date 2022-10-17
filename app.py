# from flask import Flask
# from flask_cors import CORS
import random
from pprint import pprint

# app = Flask(__name__)
# CORS(app)

# """
# Giving b number of branches and n number of nodes, distribute the branches into nodes randomly
# """

# @app.route("/randomize", method=['GET'])
# def randomize():

#     if(request.method == 'GET'):

def randomizer(nodes, branches):

    """
    STEPS
    1. Shuffle branches
    2. Distribute even n branches into m groups
    """
    #Shuffle branches
    random.shuffle(branches)

    number_of_nodes= len(nodes)
    number_of_branches= len(branches)

    #Finding even branches for nodes using the modulus operator
    even_n_branches= number_of_branches // number_of_nodes

    node_trees= []

    #distributing even n branches into nodes
    for i in range(number_of_nodes):
        node_trees.append(branches[:even_n_branches])
        del branches[:even_n_branches]

    #Distribuing uneven branches left
    uneven_branches_left= branches
    number_of_uneven_branches_left= len(branches)

    for i in range(number_of_uneven_branches_left):
        node_trees[i].append(uneven_branches_left[i])

    number_of_node_trees= len(node_trees)
    result_dict= {nodes[i]:node_trees[i] for i in range(number_of_node_trees)}

    return result_dict


def main():
    stc_names= [
        "Odumah Chidinma Silvia",
        "Odumah Stella Chidiebere",
        "Osu Steven Munachi",
        "Onuegbu Obiajulu",
        "Adams Emmanuel Ojonuewa",
        "Stephen Joseph Emeka",
        "Adesanya Ayomide Innocent",
        "Onimisi Daniella Ada",
        "Adebisi Ifeoluwa Ruth",
        "Denzel Idowu",
        "Sharon Balogun",
        "Gift Okhumode",
        "Divine Umoren",
        "MaryJane Umoren",
        "Osasere Agharese",
        "Shammah Balogun",
        "Owoele Victor",
        "Yusuff Damilola",
        "Awogbadebo Tosin",
        "Stephen Mary",
        "Adebisi Ifeoluwa",
        "Joy Godwin",
        "Goodness Israel",
        "Olajide Emmanuel",
        "Annie Christopher",
        "Samzion",
        "Daniella Sunday",
        "Bello Taiwo",
        "Bello Kehinde",
        "Anointed Okhumode",
        "Joshua Moses",
        "Audu Destiny",
        "Fatimah Abuhyahaya",
        "Maimunat Abuhyahaya",
        "Gabriella Munachimso Jacobs",
        "Awolesi Adeolwa",
        "Charles Miracle",
        "Grace Okoloise",
        "Angel Eruotor-Pat",
        "David Moore",
        "Bolu Fatuyi",
        "Samuel Chukwuemeka",
    ]
    team_leads= [
        "Promise Emmanuel",
        "Victory",
        "Michael Issac",
        "Solomon Taiwo",
        "Aladejobi David",
        "Marvelous Ogbeide",
        "Lucky Johnson",
        "Felix Destiny",
        "Attram Ayomide",
        "Fortune Ben",
        "Annie Odogwu"
    ]
    # hello= 
    result = randomizer(team_leads, stc_names)
    pprint(result)

if __name__=="__main__":
    print(main())

