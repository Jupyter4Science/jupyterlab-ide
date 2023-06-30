### examples without steps
# items from first to last
bread[first : last]
bread[first+1:last]

# items from first to the end of the array
cheese[first:]
cheese[first+1:]

# items from the beginning to last - 1
ham[:last]
ham[:last+1]

# every element of the array
bacon[:]

### examples with steps and reversals
# array[start:stop:step]
# all items reversed
orange[ : :-1]
orange[ : :-1+1]

# everything up to index reversed
cake[index: :-1]
cake[index+1: :-1]

# everything after index reversed
apple[ :index:-1]
apple[ :index+1:-1]