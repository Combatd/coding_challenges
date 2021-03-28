/*
Given matrix, a rectangular matrix of integers, 
where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).
*/

int matrixElementsSum(int[][] matrix) {
    int totalRoomSum = 0; // tracks the sum of the rooms that don't appear below a zero
    // we can be assured they are of even length 5 and 3 height
    for (int i = 0; i < matrix[0].Length; i++) {
        int currentRoomIndex = i; // the index of the current room we are checking
        // Check the current room if it contains a 0
        for(int j = 0; j < matrix.Length; j++) {
            if (matrix[j][currentRoomIndex] == 0) { 
                break;
            }
            totalRoomSum += matrix[j][currentRoomIndex];
        }
    }
    return totalRoomSum;
}

