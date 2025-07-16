# Requires "requests" to be installed (see https://pypi.org/project/requests/)
import requests

response = requests.post(
    'https://api.pixian.ai/api/v2/remove-background',
    files={'gif': open('Lbg3.gif', 'rb')},
    data={
        'test': 'true'
    },
    auth=('pxn2ed8xamq8f9c',
          'sfj3ao1ngou6jpjmj1gv32m2vueev9s2m7i4lenbpr8g50vg4e22')
)
if response.status_code == requests.codes.ok:
    # Save result
    with open('pixian_result1.gif', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
