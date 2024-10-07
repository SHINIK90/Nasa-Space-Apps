using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Linq;

public class StarSpawner : MonoBehaviour
{
    // The prefab for the stars
    public GameObject starPrefab;

    // A list of star data, you would later populate this from the CSV
    // Replace this with data parsed from your CSV file
    private List<Vector3> starPositions = new List<Vector3>();
    private List<float> starMagnitudes = new List<float>();

    // Start is called before the first frame update
    void Start()
    {
        LoadStarDataFromCSV();
        SpawnStars();
    }

    void SpawnStars(){
        for (int i = 0; i < starPositions.Count; i++)
        {
            // Instantiate star at the correct position
            GameObject star = Instantiate(starPrefab, starPositions[i], Quaternion.identity);
            
            // Adjust star size or brightness based on magnitude (lower magnitude = brighter)
            float brightnessFactor = Mathf.Clamp(2.0f / starMagnitudes[i], 0.01f, 1.0f);
            star.transform.localScale *= brightnessFactor;

            // Set the star color or shader properties based on magnitude if needed
            // Example: star.GetComponent<Renderer>().material.color = new Color(1f, 1f, 0.8f);
        }
    }
    void LoadStarDataFromCSV(){
        // Path to your CSV file, this should be changed to the actual path
        string filePath = Application.dataPath + "/StarsDatabase.csv";
        string[] dataLines = File.ReadAllLines(filePath);

        foreach (string line in dataLines.Skip(1).ToArray())
        {
            Debug.Log("read line:"+line);
            string[] data = line.Split(',');

            float ra = float.Parse(data[1]); // X coordinate from CSV
            float dec = float.Parse(data[2]); // Y coordinate from CSV
            if (!float.TryParse(data[3], out float parallax)){continue;}
            if (!float.TryParse(data[6], out float phot_g)){continue;}

            Vector3 coordinates = calculateCoordinates(ra, dec, parallax);
            float magnitude = CalculateAbsoluteMagnitude(phot_g, coordinates.magnitude); // Magnitude from CSV parsec
            // float magnitude = CalculateAbsoluteMagnitude(phot_g, parallax); // Magnitude from CSV parallax - NOT GOOD
            Debug.Log("Star created at:" + coordinates + " with brightness: " + magnitude);
            

            starPositions.Add(coordinates);
            starMagnitudes.Add(magnitude);
        }
    }
    Vector3 calculateCoordinates(float raDeg, float decDeg, float parallaxMas){
        // Convert RA and DEC from degrees to radians
        float raRad = raDeg * Mathf.Deg2Rad;
        float decRad = decDeg * Mathf.Deg2Rad;

        // Calculate the distance in parsecs from parallax (d = 1000 / parallax)
        float distance = 1000.0f / parallaxMas;

        // Calculate Cartesian coordinates
        float x = distance * Mathf.Cos(decRad) * Mathf.Cos(raRad);
        float y = distance * Mathf.Cos(decRad) * Mathf.Sin(raRad);
        float z = distance * Mathf.Sin(decRad);

        return new Vector3(x, y, z);
    }
    float CalculateAbsoluteMagnitude(float m, float d){
        return m - 5f * (Mathf.Log10(d) - 1f);
    }
}
