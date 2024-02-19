from flask import Flask, request
import requests
#CODE BY LE VAN QUOC
app = Flask(__name__)

@app.route('/')
def abc():
    return "Api By Mon Leo Hay Khok Telegram @Monleohaykhok, don't forget join https://t.me/drugsluxury"
@app.route('/api')
def get_cookies():
        cookies = request.cookies
        cookies_dict = cookies.to_dict()
        filtered_cookies = {}
        keys_to_keep = ['isGrammarlyUser', 'grauth', 'redirect_location', 'experiment_groups', 'csrf-token', 'browser_info', 'funnelType', 'gac', 'gnar_containerId', 'tdi']

        for key, value in cookies_dict.items():
            if key in keys_to_keep:
                filtered_cookies[key] = value

        headers = {
                    'authority': 'subscription.grammarly.com',
                    'accept': 'application/json',
                    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                    'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
                    'origin': 'https://account.grammarly.com',
                    'referer': 'https://account.grammarly.com/profile',
                    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'x-client-type': 'account',
                    'x-container-id': (filtered_cookies.get("gnar_containerId")),
                    'x-csrf-token': (filtered_cookies.get("csrf-token"))
                    }

        try:
            response = requests.get('https://subscription.grammarly.com/api/v2/subscription', headers=headers)
            if response.status_code==200:
                data = response.json()
                is_premium = data.get('isPremium')
                if is_premium == False:
                    return "Soucre Code By VannQuoc IS ME"
                else:
                    return "Mua Full Source Code Inbox Telegram:@MonLeoHayKhok"
        except ValueError as e:
            print(f"Error parsing JSON: {e}")

        return "Error"
@app.route('/check')
def check_acc():
        cookies = request.cookies
        cookies_dict = cookies.to_dict()
        filtered_cookies = {}
        keys_to_keep = ['isGrammarlyUser', 'grauth', 'redirect_location', 'experiment_groups', 'csrf-token', 'browser_info', 'funnelType', 'gac', 'gnar_containerId', 'tdi']

        for key, value in cookies_dict.items():
            if key in keys_to_keep:
                filtered_cookies[key] = value

        headers = {
                    'authority': 'subscription.grammarly.com',
                    'accept': 'application/json',
                    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                    'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
                    'origin': 'https://account.grammarly.com',
                    'referer': 'https://account.grammarly.com/profile',
                    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                    'x-client-type': 'account',
                    'x-container-id': (filtered_cookies.get("gnar_containerId")),
                    'x-csrf-token': (filtered_cookies.get("csrf-token"))
                    }

        try:
            response = requests.get('https://auth.grammarly.com/v3/user?app=account&field=frontend_role&field=frontend_teamType&field=frontend_industryType&field=frontend_companySize&field=frontend_graduationYear&field=frontend_seniority&permissions=all', headers=headers)
            if response.status_code == 200:
                response_json = response.json()
                email = response_json.get("email", "")
                login_type = response_json.get("loginType", "")
                grammaly_edu = response_json.get("grammarlyEdu", "")
                return f'EMAIL: {email} Login Type: {login_type} Grammarly Edu:{grammaly_edu}'
        except ValueError as e:
            print(f"Error parsing JSON: {e}")
if __name__ == '__main__':
        app.run(host='0.0.0.0')
