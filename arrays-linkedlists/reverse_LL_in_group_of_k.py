'''
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, 
in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse(head):
        curr,prev=head,None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
    if(k==1):
        return head
    length=1
    first=head
    temp=head
    dummy=ListNode(0)
    res=dummy
    while(temp.next):
        temp=temp.next
        length+=1
        if(length==k):
            nextnode=temp.next
            temp.next=None
            res.next=reverse(first)
            res=first
            first=nextnode
            temp=first
            length=1
            if(not first):
                break
    if(first): #last group unchanged
        res.next=first
    return dummy.next
