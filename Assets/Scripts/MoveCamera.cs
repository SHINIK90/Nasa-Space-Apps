using UnityEngine;

public class MoveCamera : MonoBehaviour
{
    public Vector3 positionA; // Starting position (A)
    public Vector3 positionB; // Target position (B)
    public Vector3 rotationA; // Starting rotation (A)
    public Vector3 rotationB; // Target rotation (B)
    public float timeToMove = 1.0f; // Time to move and rotate from A to B (T)
    public float delayBeforeMove = 2.0f; // Delay before moving and rotating (X)

    private bool moveStarted = false; // To track if movement has started
    private float elapsedTime = 0f; // To track time during movement

    // Start is called before the first frame update
    void Start()
    {
        // Set the initial position and rotation of the camera
        transform.position = positionA;
        // transform.rotation = rotationA;

        // Start the movement and rotation after delay
        Invoke("StartMoving", delayBeforeMove);
    }

    // This function will be called after the delay
    void StartMoving()
    {
        moveStarted = true;
    }

    // Update is called once per frame
    void Update()
    {
        if (moveStarted)
        {
            // Move camera from A to B over time T
            if (elapsedTime < timeToMove)
            {
                elapsedTime += Time.deltaTime;
                float percentageComplete = elapsedTime / timeToMove;

                // Move the position
                transform.position = Vector3.Lerp(positionA, positionB, percentageComplete);

                // Rotate the camera
                Quaternion startRotation = Quaternion.Euler(rotationA);
                Quaternion endRotation = Quaternion.Euler(rotationB);
                transform.rotation = Quaternion.Lerp(startRotation, endRotation, percentageComplete);
            }
        }
    }
}
