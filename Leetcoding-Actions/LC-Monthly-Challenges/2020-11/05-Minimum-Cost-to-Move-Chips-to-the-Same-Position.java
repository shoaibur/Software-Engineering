class Solution {
    public int minCostToMoveChips(int[] position) {
        /*
        Idea: Move all even positioned chips to 0, i.e., count them and 
        all odd positioned chips to 1, i.e., count them; take min of two counts
        T: O(n) and S: O(1)
        */
        int zeroCost = 0;
        int oneCost = 0;
        
        for (int i = 0; i < position.length; i++) {
            if (position[i] % 2 == 0)
                zeroCost++;
            else
                oneCost++;
        }
        return Math.min(zeroCost, oneCost);
    }
}
