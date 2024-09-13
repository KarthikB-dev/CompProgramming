class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> output;
        map<double, vector<vector<int>>> dist_to_point;
        for (auto& point : points) {
            double curr_dist = point[0] * point[0] + point[1] * point[1];
            if (dist_to_point.count(curr_dist) > 0) {
               dist_to_point[curr_dist].push_back(point); 
            }
            else {
                dist_to_point[curr_dist] = {point};
            }
        }
        int iters = 1;
        for (auto& kv_pair : dist_to_point) {
            for (auto& point : kv_pair.second) {
                if (iters > k) {
                    break;
                }
                output.push_back(point);
                iters += 1;
            }
        }
        return output; 
    }
};