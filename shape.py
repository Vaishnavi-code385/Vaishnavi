import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Creating a logger
logger = logging.getLogger(__name__)
rows=int(input("Enter no of rows"))
logging.info(f"no of rows {rows}")
pattern=input("Enter pattern symbol")

for i in range(1,rows+1):
    print(pattern*i)