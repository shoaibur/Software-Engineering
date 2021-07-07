class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        /*
        states ^ pigs >= buckets
        pigs >= log(buckets) / log(states)
        T: O(1) and S: O(1)
        */
        int states = minutesToTest / minutesToDie + 1;
        return (int) (Math.ceil(Math.log(buckets) / Math.log(states)));
    }
}
