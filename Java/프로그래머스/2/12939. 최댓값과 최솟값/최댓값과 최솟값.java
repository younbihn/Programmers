class Solution {
    public String solution(String s) {
        String[] S = s.split(" ");
        
        int min = Integer.parseInt(S[0]);
        int max = Integer.parseInt(S[1]);
        
        for (int i = 0; i < S.length; i++) {
            int current = Integer.parseInt(S[i]);
            
            if (current < min) {
                min = current;
            }
            if (current > max) {
                max = current;
            }
        }
        
        return min + " " + max;
    }
}