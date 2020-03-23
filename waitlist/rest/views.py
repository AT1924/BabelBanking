from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import sqlite3

#
# Class WaitlistView: When a GET request to this view is called it returns
# information about the number of people in line to display on the html page
#
class WaitlistView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """
        Returns the number of people who have joined the waitlist.
        """
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        place = c.execute('SELECT MAX(place) FROM users').fetchone()
        conn.close()
        return Response({'waitlist_length': place})

#
# Class SignUpView: When a GET request to this view is called information about the
# user, username/referenceNumber, is passed to the backend where it is processed, checked for
# errors, and ultimately submitted into the database. If the reference number is valid then
# the place of the user that the reference number belonged to is increased by one.
#
class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """
        Method that takes in a request object containing the username and reference number of the
        user signing up.
        """

        query_string = request.META["QUERY_STRING"].split("&")
        username = query_string[0].split("=")[1]
        refNumber = query_string[1].split("=")[1]

        username = (username,)
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', username)


        # if the username already in database
        if (c.fetchone() != None):
            return Response({'error': "ERROR: that username is already taken"})


        else:
            if (refNumber != ''):
                link = (refNumber,)
                c.execute('SELECT place from users WHERE link=?', link)
                refPlace = c.fetchone()
                # if ref number is not valid
                if (refPlace == None):
                    return Response({'error': "ERROR: Not a valid Reference Number"})
                ##
                ## This is the code that swaps places when given a reference number. Right now it
                ## increases the place of the reference number owner by 1.
                ##
                exchangePlace = refPlace[0] - 1
                if (refPlace != None and exchangePlace != 0):

                    exchangeData1 = (refPlace[0], exchangePlace)
                    exhangeData2 = (exchangePlace, link[0])
                    c.execute('UPDATE users SET place=? WHERE place=?', exchangeData1)
                    c.execute('UPDATE users SET place=? WHERE link=?', exhangeData2)


            place = c.execute('SELECT MAX(place) FROM users').fetchone()
            place = place[0] + 1
            linkNumber = get_random_string()
            linkMessage = "Reference Number is : " + linkNumber
            username = username[0]

            user = [(username, place, linkNumber)]
            c.executemany('INSERT INTO users (username, place, link) VALUES (?,?,?)', user)

        conn.commit()
        conn.close()
        return Response({'waitlist_length': place, 'linkNumber': linkMessage})
