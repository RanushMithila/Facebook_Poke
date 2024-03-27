import requests as req
import json

my_user_id = "YOUR USER ID"

def poke_one(user_id, my_user_id):
    poke_body = f"av={my_user_id}&__aaid=0&__user={my_user_id}&__a=1&__req=15&__hs=19809.HYP%3Acomet_pkg.2.1..2.1&dpr=1.5&__ccg=GOOD&__rev=1012348741&__s=xsvtr0%3Act93zd%3Atsa01y&__hsi=7351077574154155609&__dyn=7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwnUW3q2ibwNw9G2Sawba1DwUx60GE3Qwb-q7oc81xoswMwto886C11wBz83WwtohwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5o7G4-5pUfEe88o4Wm7-2K0-poarCwLyES1Iwh85d08O321LyUaUcojxK2B08-269wqQ1FwgU4q3G1eKufxa3m7E&__csr=hO79lPPq4mPmC-CgIy6lbdt9cAp4N2YDRskDITjA9kkBELKQa9BuH4TOqIzRRTLmRJABGtGBGmjhaAyGGAh4BgknzUReQeAAAyqxp2V8V2emhqCiUFF24byEWiF8qAJah5ABCxi8wwBwIxW8gizEoG1Ey8lG2q2CbzUsUyU5W361Ywr8S9weu5F84e0TEuxSi0-85O0KE15oeE0-q0hW064o1nU4Tw0nQ_w0eJK0azw2nVGg0NR11dk0rV03M8jwMxy08twbi046o0Ea05-po0gMw0BRwDw0k3E4Ovqwehw8u&__comet_req=15&fb_dtsg=NAcMGyLYNSJx0IWZrhXlHPHAFydldn4r1Q6bYo7XhbTuKhuuOA1fiBQ%3A42%3A1711259714&jazoest=25531&lsd=9MyC-_-uCD8ivGemIg2yxt&__spin_r=1012348741&__spin_b=trunk&__spin_t=1711556123&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PokesMutatorPokeMutation&variables=%7B%22input%22%3A%7B%22client_mutation_id%22%3A%221%22%2C%22actor_id%22%3A%22{my_user_id}%22%2C%22user_id%22%3A%22{user_id}%22%7D%7D&server_timestamps=true&doc_id=5028133957233114"
    return poke_body

def poke(data):
    edges = data["data"]["viewer"]["incoming_pokes"]["edges"]
    found = False
    for edge in edges:
        if edge["node"]["poker"]["poke_status"] == "CAN_POKE":
            found = True
            print(edge["node"]["poker"]["id"])
            send_data = poke_one(edge["node"]["poker"]["id"], my_user_id)
            res = req.post(url=url, data=send_data, headers=header)
            print(res.text)

    if (~found):
        print("No new Pokes")


url = "https://www.facebook.com/api/graphql/"
header = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Brave\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "x-asbd-id": "129477",
    "x-fb-friendly-name": "PokesMutatorPokeMutation",
    "x-fb-lsd": "W1KCiD8aoVJXcClDSKithp",
    "cookie": "ADD YOUR COOKIE HERE",
    "Referer": "https://www.facebook.com/pokes/?notif_id=1709468248375460&notif_t=poke&ref=notif",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

get_poke_list_body = f"av={my_user_id}&__aaid=0&__user={my_user_id}&__a=1&__req=2a&__hs=19809.HYP%3Acomet_pkg.2.1..2.1&dpr=1.5&__ccg=MODERATE&__rev=1012348741&__s=rtun13%3Aou34le%3Ap4twml&__hsi=7351073133677649756&__dyn=7AzHK4HwBgDx-5Q1ryaxG4Qih09y2O5U4e2C3-ubyQdwSAx-bwNwnof8boG4E762S1DwUx60xU8k1sw9u0LVEtwMw65xO2OU7m2210wEwgo9oO0wE7u12wOx62G5Usw9m1cwLwBgK7o8417wc61awkovwRwlE-U2exi4UaEW4UWu1jxS6FobrwKxm5oe8cEW4-5pUfEdbwxwhFVovUaU3qxWm2CVEbUGdwr84i223908O3216xi4UK2K364UrwFgbU5-269wkopg6C13whEeEfE-VU-4Edouw&__csr=gaseNJgxd1jPgD2dsbH4YIGRdlRFhkl94jhsXnOfEJlcBmTOJh2Rfah4XhkrHlCy9WlGQimFDDpay94TBqVfACH_Ah5Gp9Wh6CLqgKlDAhd4jGuQmKRq9GjKq59S-ayWXypoh_jLBUHLCiy9HyF8OqGzpqGidy9ahoN6ACy8GqWxm9Cmdxyavyk4rC-qVVGzEW9zXByEcu2KA2y263CjAxCczk8AxJe3mQ2iu2mmFEmz4l2WAwwxOewEyokwwwWg8oWezVUlAzpFo_whESKE88nwRwGh8Si68iz-4k5EG8wJzkeyUfWBwSwl8imu58ScwJyp8sDwgEc98fAq4oiyUjAwNwmSXyoGmJlktmn4WwjoWh1eq4EcBypQbwEx1hddr5Uj4aE9EGFcwrxsEC68kjwk_iwprwloO0Q84i0GDIg0zo9UtwgE2qw6TxO19QnQU8UswEwMwlU4aagOcxhp8SmaCQXU6u08ow3Yo0qvhyb9y6nzEG0Bu0cfw65yo1qA0bZg3r-1Txe680pUw2j44Q3S00A9Gw0POw2EU0B-qA1HwuE5G0GocGwfJ11dk0rV03Me4oaV8OVU17rTwcZ5xW0J80_efxm0No1L80yC0bwweWm0zVomwl41rw7FwiA0CU2sw13q2u0hu2e0cZwDw3HEtG2O04Po0LObg-1bw5axQw0oiwlVE4Ovqwehw8u1ho1xo0W606GE0DC09ww&__comet_req=15&fb_dtsg=NAcPFY8uCffe8A53F0wc3UIIcQeLci1NfWKl-cS6Z7YHJLVPDlLNM2Q%3A42%3A1711259714&jazoest=25106&lsd=5VjCMU5cYY5DCCX6C0Q6gz&__spin_r=1012348741&__spin_b=trunk&__spin_t=1711555089&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PokesSurfaceQuery&variables=%7B%22scale%22%3A1.5%7D&server_timestamps=true&doc_id=6433741240081581"

res = req.post(url=url, data=get_poke_list_body, headers=header)

data = json.loads(res.text)
poke(data)
