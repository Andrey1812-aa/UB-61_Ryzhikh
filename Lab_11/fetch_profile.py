import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile(login):
    if not login.strip():
        raise ValueError('Пустой логин')
    url = 'https://api.github.com/users/' + quote(login.strip(), safe='')
    request = Request(url, headers={'Accept': 'application/vnd.github+json',
                                    'User-Agent': 'python-course-lab11'})
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('login'), str):
        raise ValueError('Ответ не является профилем')
    return data


def main():
    folder = Path(__file__).resolve().parent
    try:
        data = fetch_profile(input('Логин GitHub: '))
        with open(folder / 'profile.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print('Профиль сохранён:', data['login'])
    except HTTPError as error:
        print('Код HTTP:', error.code)
    except (URLError, TimeoutError, socket.timeout):
        print('Ошибка сети')
    except (ValueError, UnicodeError) as error:
        print('Ошибка данных:', error)
    except OSError as error:
        print('Ошибка доступа:', error)


if __name__ == '__main__':
    main()
