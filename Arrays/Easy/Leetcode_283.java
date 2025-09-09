import java.util.Arrays;
class Leetcode_283 {
    public static void main(String[] args) {
        int[] num = { 0, 1, 0, 3, 12 };
        moveZeroes(num);
    }

    public static void moveZeroes(int[] nums) {
        int left = 0, right = 0;
        int[] leftArr = new int[nums.length];
        int[] rightArr = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                rightArr[right] = 0;
                right++;
            } else {
                leftArr[left] = nums[i];
                left++;
            }
        }
        // Copy non-zero elements from leftArr
        for (int i = 0; i < left; i++) {
            nums[i] = leftArr[i];
        }
        // Copy zeros from rightArr
        for (int i = 0; i < right; i++) {
            nums[left + i] = rightArr[i];
        }
        System.out.println(Arrays.toString(nums));
    }
}