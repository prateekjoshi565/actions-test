import os

def main():
  print("Hello from github actions!")
  my_key = os.environ.get("MY_SECRET_KEY")
  
  if not my_key:
    raise RuntimeError("MY_SECRET_KEY env var is not set!")
  
  print("All good!")
  
if __name__ == '__main__':
  main()
