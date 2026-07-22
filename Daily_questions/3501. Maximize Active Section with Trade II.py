class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n) if self.n > 0 else []
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node + 1, start, mid)
        self._build(data, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, ql, qr):
        if ql > end or qr < start:
            return 0
        if ql <= start and end <= qr:
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(2 * node + 1, start, mid, ql, qr)
        right_max = self.query(2 * node + 2, mid + 1, end, ql, qr)
        return max(left_max, right_max)

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        zero_groups = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zero_groups.append((start, i - 1, i - start))
            else:
                i += 1
                
        num_groups = len(zero_groups)
        A = []
        for k in range(num_groups - 1):
            A.append(zero_groups[k][2] + zero_groups[k + 1][2])
            
        seg_tree = SegmentTree(A)
        
        group_starts = [g[0] for g in zero_groups]
        group_ends = [g[1] for g in zero_groups]
        
        ans = []
        
        for l, r in queries:
            
            idx_l = bisect_left(group_ends, l)
            idx_r = bisect_right(group_starts, r) - 1
             
            if idx_l >= idx_r or idx_l >= num_groups or idx_r < 0:
                ans.append(total_ones)
                continue
            
            left_len = min(zero_groups[idx_l][1], r) - max(zero_groups[idx_l][0], l) + 1
            right_len = min(zero_groups[idx_r][1], r) - max(zero_groups[idx_r][0], l) + 1
            max_gain = 0
            
            if idx_l + 1 <= idx_r:
                if idx_l + 1 == idx_r:
                    max_gain = max(max_gain, left_len + right_len)
                else:
                    max_gain = max(max_gain, left_len + zero_groups[idx_l + 1][2])
                    
            if idx_r - 1 >= idx_l and idx_r - 1 != idx_l:
                max_gain = max(max_gain, zero_groups[idx_r - 1][2] + right_len)
                
            if idx_l + 1 <= idx_r - 2:
                st_max = seg_tree.query(0, 0, len(A) - 1, idx_l + 1, idx_r - 2)
                max_gain = max(max_gain, st_max)
                
            ans.append(total_ones + max_gain)
            
        return ans