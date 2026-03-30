class Solution {

    public String encode(List<String> strs) {
        String s = "";
        for (String st : strs) {
            s += st;
            s += "///";
        }
        return s;
    }

    public List<String> decode(String str) {
        if (str.equals("")) return new ArrayList<String>();
        if (str.equals("///")) return Arrays.asList("");
        return Arrays.asList(str.split("///"));
    }
}
