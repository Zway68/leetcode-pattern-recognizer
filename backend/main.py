from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello Weiwei, keep coding!'}

@app.get('/pattern/{problem_id}')
def get_pattern(problem_id: int):
    # Mock data for now
    patterns = {
        1: 'Two Sum -> Hash Map',
        200: 'Number of Islands -> DFS/BFS',
        121: 'Best Time to Buy and Sell Stock -> Sliding Window',
        3: 'Longest Substring Without Repeating Characters -> Sliding Window'
    }
    return {'problem_id': problem_id, 'pattern': patterns.get(problem_id, 'Unknown Pattern')}

