using UnityEngine;

public class ScreenshotManager : MonoBehaviour
{
    string screenshotPath = "C:/Users/LuisC/Desktop/unity_screenshot/";
    public float screenshotInterval = 1f; // Interval in seconds between each screenshot

    private float timer = 0f;

    void Update()
    {
        timer += Time.deltaTime;


        if (Input.GetKeyDown(KeyCode.S) || (timer >= screenshotInterval))
        {
            CaptureScreenshot();
            timer = 0f;
        }
    }

    void CaptureScreenshot()
    {
        //string timestamp = System.DateTime.Now.ToString("yyyyMMddHHmmss");
        //string filename = screenshotPath + "screenshot_" + timestamp + ".png";
        string filename = screenshotPath + "screenshot_" + "base" + ".png";
        ScreenCapture.CaptureScreenshot(filename);
        Debug.Log("Screenshot captured: " + filename);
    }
}