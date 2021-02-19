class b_search:
    def find(arr, tar):
        head = 0
        tail = len(arr)-1
        while head < tail:
            mid = head + (tail-head)//2
            if arr[mid] == tar:
                return True
            elif arr[mid] < tar:
                head = mid+1
            else:
                tail = mid-1
        return False
