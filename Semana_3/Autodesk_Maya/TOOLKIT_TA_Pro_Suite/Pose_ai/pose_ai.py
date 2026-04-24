import requests
import json
import os

POSE_FOLDER = os.path.join(os.path.dirname(__file__), "poses")

class PoseAI:

    def get_all_poses(self):

        poses = []

        for file in os.listdir(POSE_FOLDER):
            if file.endswith(".json"):
                with open(os.path.join(POSE_FOLDER, file)) as f:
                    poses.append(json.load(f))

        return poses

    def choose_pose(self, prompt):

        poses = self.get_all_poses()

        pose_names = [p["name"] for p in poses]

        API_KEY = "TU_API_KEY"

        url = "https://api.openai.com/v1/responses"

        data = {
            "model": "gpt-4.1-mini",
            "input": f"""
            Given this animation prompt:

            {prompt}

            Choose the best pose from this list:

            {pose_names}

            Return ONLY the pose name.
            """
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            r = requests.post(url, headers=headers, json=data)
            result = r.json()

            return result["output"][0]["content"][0]["text"].strip()

        except:
            return pose_names[0]