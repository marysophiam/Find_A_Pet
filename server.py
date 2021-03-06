from flask import Flask, render_template, request

import petfinder

from petfinder.exceptions import LimitExceeded

from api_key import API_KEY, API_SECRET

from urllib2 import urlopen

from json import load

app = Flask(__name__)

api = petfinder.PetFinderClient(api_key=API_KEY, api_secret=API_SECRET)

# response = urlopen(api)

# json_obj = load(response)

# print json_obj
# response = urlopen(api)

# json_obj = load(response)

# print json_obj

@app.route("/")
def find_a_pet():
   
    return render_template("index.html")


@app.route("/results")
def return_results():

    animal = request.args.get("animal")
    zipcode = request.args.get("zipcode")

    pet_ids = []
    # pet_names = []

    try:
        received_count = 0

        for pet in api.pet_find(
                animal=animal, location=zipcode, output="basic", count=10
                ):
            # print ("%s - %s" % (pet["id"], pet["name"]))

            received_count += 1
            pet_ids.append(pet)

            if received_count > 10:
                break

    except LimitExceeded:
        pass


    return render_template("results.html", pets=pet_ids)


if __name__ == "__main__":
    app.run(debug = True)



# pet.find
# Searches for pets according to the criteria you provde and returns a
# collection of pet records matching your search. The results will contain
# at most count records per query, and a lastOffset tag. To retrieve the
# next result set, use the lastOffset value as the offset to the next
# pet.find call.


# Name        Type    Required?   Description

# key         string  required        your developer key

# animal      string  optional        type of animal
#                                     (barnyard, bird, cat, dog, horse,
#                                     pig, reptile, smallfurry)

# location    string  required        the ZIP/postal code or city and state
#                                     where the search should begin

# count       integer optional        how many records to return for this 
#                                     particular API call (default is 25)

# output      string  optional        how much of each record to return:
#                     (default=basic) basic (no description) or full
#                                     (includes description)

# format      string  optional        Response format: xml, json
#                     (default=xml) 



# http://petfinder-api.readthedocs.io/en/latest/

# import petfinder

# # Instantiate the client with your credentials.
# api = petfinder.PetFinderClient(api_key='yourkey', api_secret='yoursecret')

# # Search for pets.
# for pet in api.pet_find(
#     animal="dog", location="29678", output="basic",
#     breed="Treeing Walker Coonhound", count=200,
# ):
#     print("%s - %s" % (pet['id'], pet['name']))


# higa602@gmail.com
