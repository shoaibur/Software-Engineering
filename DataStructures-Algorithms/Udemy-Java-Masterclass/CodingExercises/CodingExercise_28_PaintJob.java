public class PaintJob {
    public static int getBucketCount(double width, double height, double areaPerBucket, int extraBuckets) {
        if (height <= 0 || width <= 0 || areaPerBucket <= 0 || extraBuckets < 0) return -1;
        double area = width * height;
        int totalBuckets = (int) (area / areaPerBucket);
        return totalBuckets - extraBuckets + 1;
    }
    
    public static int getBucketCount(double width, double height, double areaPerBucket) {
        if (height <= 0 || width <= 0 || areaPerBucket <= 0) return -1;
        double area = width * height;
        int totalBuckets = (int) (area / areaPerBucket);
        return totalBuckets + 1;
    }
    
    public static int getBucketCount(double area, double areaPerBucket) {
        if (area <= 0|| areaPerBucket <= 0) return -1;
        int totalBuckets = (int) (area / areaPerBucket);
        return totalBuckets + 1;
    }
}
