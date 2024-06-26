import redis

def fetch_robots(url: str) -> str | None:
	try:
		conn = redis.Redis(host='localhost', port=6379, db=0)
		robots = conn.get(url)
		conn.close()
		return str(robots)
	except Exception as e:
		print(f'\tThere was an error fetching the robots.txt of {url}: {e}')


def add_robots(url: str, robots: str):
	try:
		conn = redis.Redis(host='localhost', port=6379, db=0)
		conn.set(url, robots)
		conn.close()
	except Exception as e:
		print(f'\tThere was an error adding the robots.txt of {url}: {e}')