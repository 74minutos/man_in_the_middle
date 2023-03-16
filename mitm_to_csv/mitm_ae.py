import csv
from mitmproxy import http
from urllib.parse import urlparse


session = input('qué nombre quieres darle a tu sesión? ')
system = input('qué sistema vas a debuggear? (google analytics, tealium) ')

if system == 'google analytics':
    #google analytics
    def response(flow: http.HTTPFlow):
        u = urlparse(flow.request.url)
        if u.netloc == 'www.google-analytics.com':
            print('GOOGLE ANALYTICS')
            with open('session_{}.csv'.format(session), mode='a') as session_user:
                session_writer = csv.writer(session_user, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                session_writer.writerow([u.query])

elif system == 'tealium':
    #tealium
    def response(flow: http.HTTPFlow):
        u = urlparse(flow.request.url)
        if u.netloc == 'collect-eu-central-1.tealiumiq.com':
            with open('session_{}.csv'.format(session), mode='a') as session_user:
                session_writer = csv.writer(session_user, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                session_writer.writerow([flow.request.content])
