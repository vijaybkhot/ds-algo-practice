class Solution {
    public String reverseWords(String s) {
        // Split by space
        String[] words = s.split(" ");

        // Use StringBuilder to build the result
        StringBuilder sb = new StringBuilder();

        // Iterate in reverse and skip empty strings (due to multiple spaces)
        for (int i = words.length - 1; i >= 0; i--) {
            if (!words[i].isEmpty()) {
                sb.append(words[i]);
                sb.append(" ");
            }
        }

        // Remove the trailing space
        return sb.toString().trim();
        
    }
}