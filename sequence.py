

def sequence_preprocess(data, input_length, output_length):
    if input_length > len(data) or output_length > len(data):
        raise ValueError('Sequence length cannot be longer than data')

    input_sequences, output_sequences = [], []
    for i in range(len(data) - input_length - output_length):
        input_sequences.append(data[i:i + input_length])
        output_sequences.append(data[i+input_length:i+input_length+output_length])

    return input_sequences, output_sequences
