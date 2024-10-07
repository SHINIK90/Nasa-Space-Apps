using UnityEngine;

public class StarBrightnessController : MonoBehaviour
{
    public ComputeShader starBrightnessShader;
    public GameObject cameraObject;
    
    struct Star {
        public Vector3 position;
        public float intrinsicBrightness;  // M value
        public float calculatedBrightness; // Output: Calculated brightness
    }

    Star[] stars;
    ComputeBuffer starBuffer;
    int kernelHandle;

    void Start()
    {
        // Initialize the stars array with actual data
        stars = new Star[10000]; // Example: 10,000 stars
        
        for (int i = 0; i < stars.Length; i++) {
            // Fill this with actual positions and intrinsic brightness data
            stars[i].position = new Vector3(Random.Range(-1000, 1000), Random.Range(-1000, 1000), Random.Range(-1000, 1000));
            stars[i].intrinsicBrightness = Random.Range(0.1f, 5.0f);  // Random example brightness
            stars[i].calculatedBrightness = 0f; // To be calculated
        }
        
        // Create a compute buffer to hold the star data
        starBuffer = new ComputeBuffer(stars.Length, sizeof(float) * 6); // 3 floats for position, 1 for intrinsic brightness, 1 for calculated brightness
        starBuffer.SetData(stars);
        
        // Get the kernel handle for the compute shader
        kernelHandle = starBrightnessShader.FindKernel("CSMain");
        
        // Set the star buffer on the compute shader
        starBrightnessShader.SetBuffer(kernelHandle, "starBuffer", starBuffer);
    }

    void Update()
    {
        // Get the camera position in world space
        Vector3 cameraPos = cameraObject.transform.position;

        // Pass the camera position to the compute shader
        starBrightnessShader.SetVector("cameraPosition", cameraPos);

        // Execute the compute shader
        starBrightnessShader.Dispatch(kernelHandle, stars.Length, 1, 1);

        // Retrieve the updated star data if needed (for rendering or further use)
        starBuffer.GetData(stars);

        // Apply the updated brightness to your stars (in your rendering logic)
        // For example, you could modify the material of each star based on the calculated brightness
    }

    void OnDestroy()
    {
        // Release the compute buffer
        starBuffer.Release();
    }
}
