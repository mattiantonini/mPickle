try:
    import micropython #MicroPython
    import mpickle as pickle
    from ulab import numpy as np, dtype

    import register_pickle_funcs

    pickle.mpickle.DEBUG_MODE = False
except ImportError: #CPython
    import pickle
    import numpy as np
    from numpy import dtype

def serialize_and_deserialize(obj):
    """
    This function attempts to serialize and deserialize the given object using the pickle module.
    If successful, it prints the serialized byte stream, the deserialized object, and verifies 
    if the deserialized object matches the original.

    Parameters:
    obj (any): The Python object to be serialized and deserialized.
    """
    try:
        serialized = pickle.dumps(obj)
        print(f"Serialized ({len(serialized)} bytes): \n\n{serialized}\n")
        deserialized = pickle.loads(serialized)
        print(f"Deserialized: {deserialized}")
        if type(obj) is list:
            print(f"\nObjects match? {obj == deserialized}")
        else:
            print(f"\nObjects match? {list(obj.tolist()) == list(deserialized.tolist())}")
    except Exception as e:
        print(f"Error with {obj}: {e}")

def main():
    test_array = [int(x) for x in range(64)]
    test_objects = [
        np.array(test_array, dtype=dtype('int16')),                     # 1D array with 16 elements
        np.array(test_array, dtype=dtype('int16')).reshape((8,8)),      # 2D array (4x4) with 16 elements
        np.array(test_array, dtype=dtype('int16')).reshape((4,4,4)),    # 3D array (4x2x2) with 16 elements
        np.array(test_array, dtype=dtype('int16')).reshape((4,2,2,4)),  # 4D array (2x2x2x2) with 16 elements
    ]
    
    # Serialize individual test objects
    for obj in test_objects:
        print(f"Testing Object: {obj} (Type: {type(obj)})")
        serialize_and_deserialize(obj)
        print("\n" + "="*50)

    # # Serialize the entire list of test objects
    print("Testing all objects as a single collection")
    serialize_and_deserialize(test_objects)

if __name__ == "__main__":
    main()