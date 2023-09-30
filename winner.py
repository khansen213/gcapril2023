from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_winner', methods=['POST'])
def check_winner():
    user_name = request.form.get('name')

    # Check if 'winner.txt' already contains a winner
    with open('winner.txt', 'r') as file:
        existing_winner = file.readline().strip()

    if existing_winner:
        return jsonify({'message': 'There is already a winner: ' + existing_winner})
    else:
        # Write the winner's name to 'winner.txt'
        with open('winner.txt', 'w') as file:
            file.write(user_name)
        return jsonify({'message': 'Winner saved: ' + user_name})

if __name__ == '__main__':
    app.run(debug=True)
