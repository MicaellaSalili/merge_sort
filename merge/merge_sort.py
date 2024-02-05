from flask import Flask, render_template, request

app = Flask(__name__)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

@app.route('/')
def index():
    return render_template('merge_sort.html')

@app.route('/sort', methods=['POST'])
def sort():
    if request.method == 'POST':
        input_array = request.form['input_array']
        arr = [int(x) for x in input_array.split(',')]
        mergeSort(arr)
        sorted_array = arr
        return render_template('merge_sort.html', input_array=input_array, sorted_array=sorted_array)

if __name__ == '__main__':
    app.run(debug=True)
