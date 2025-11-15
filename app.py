from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/random-number', methods=['GET'])
def get_random_number():
    try:
        # get min and max (only int's supported)
        min_val = request.args.get('min', type=int)
        max_val = request.args.get('max', type=int)
        

        # only min provided
        if min_val is not None and max_val is None:
            return jsonify({'error': 'if min value is provided, max value must also be provided'}), 400
        
        # default to range of 1-20
        if (min_val and max_val) is None:
            min_val = 1
            max_val = 20
        
        # min value defaults to 1 if not provided
        elif min_val is None and max_val is not None:
            min_val = 1
        
        # min must be less than max
        if min_val > max_val:
            return jsonify({'error': 'min value greater than max value'}), 400
        
        random_number = random.randint(min_val, max_val)
        
        return jsonify({
            'min': min_val,
            'max': max_val,
            'number': random_number
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
