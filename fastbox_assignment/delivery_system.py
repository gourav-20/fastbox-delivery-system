import json
import math

# ==================================
# LOAD FILE
# ==================================

file_name = input(
    "Enter JSON file path (or press Enter for base_case.json): "
).strip()

if file_name == "":
    file_name = "base_case.json"

with open(file_name, "r") as file:
    data = json.load(file)

# ==================================
# NORMALIZE WAREHOUSES
# ==================================

if isinstance(data["warehouses"], list):

    warehouses = {}

    for warehouse in data["warehouses"]:
        warehouses[
            warehouse["id"]
        ] = warehouse["location"]

else:

    warehouses = data["warehouses"]

# ==================================
# NORMALIZE AGENTS
# ==================================

if isinstance(data["agents"], list):

    agents = {}

    for agent in data["agents"]:
        agents[
            agent["id"]
        ] = agent["location"]

else:

    agents = data["agents"]

# ==================================
# NORMALIZE PACKAGES
# ==================================

packages = []

for package in data["packages"]:

    warehouse_id = (
        package.get("warehouse")
        or package.get("warehouse_id")
    )

    packages.append({
        "id": package["id"],
        "warehouse": warehouse_id,
        "destination": package["destination"]
    })

# ==================================
# DISTANCE FUNCTION
# ==================================

def calculate_distance(point1, point2):

    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

# ==================================
# AGENT STATISTICS
# ==================================

agent_stats = {}

for agent_id in agents:

    agent_stats[agent_id] = {
        "packages_delivered": 0,
        "total_distance": 0
    }

# ==================================
# PACKAGE ASSIGNMENT
# ==================================

assignments = []

for package in packages:

    warehouse_location = (
        warehouses[package["warehouse"]]
    )

    nearest_agent = None
    nearest_location = None

    min_distance = float("inf")

    # Find nearest agent

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        if distance < min_distance:

            min_distance = distance
            nearest_agent = agent_id
            nearest_location = agent_location

    # Pickup distance

    pickup_distance = calculate_distance(
        nearest_location,
        warehouse_location
    )

    # Delivery distance

    delivery_distance = calculate_distance(
        warehouse_location,
        package["destination"]
    )

    total_distance = (
        pickup_distance +
        delivery_distance
    )

    assignments.append({
        "package_id": package["id"],
        "agent_id": nearest_agent,
        "distance": round(total_distance, 2)
    })

    agent_stats[
        nearest_agent
    ]["packages_delivered"] += 1

    agent_stats[
        nearest_agent
    ]["total_distance"] += total_distance

# ==================================
# EFFICIENCY
# ==================================

best_agent = None
best_efficiency = float("inf")

for agent_id in agent_stats:

    packages_count = (
        agent_stats[agent_id]
        ["packages_delivered"]
    )

    total_distance = (
        agent_stats[agent_id]
        ["total_distance"]
    )

    if packages_count > 0:

        efficiency = (
            total_distance /
            packages_count
        )

    else:

        efficiency = 0

    efficiency = round(
        efficiency,
        2
    )

    agent_stats[agent_id][
        "total_distance"
    ] = round(
        total_distance,
        2
    )

    agent_stats[agent_id][
        "efficiency"
    ] = efficiency

    if (
        packages_count > 0 and
        efficiency < best_efficiency
    ):

        best_efficiency = efficiency
        best_agent = agent_id

# ==================================
# REPORT
# ==================================

report = {
    "assignments": assignments,
    "agent_statistics": agent_stats,
    "best_agent": best_agent
}

with open(
    "report.json",
    "w"
) as file:

    json.dump(
        report,
        file,
        indent=4
    )

# ==================================
# OUTPUT
# ==================================

print("\nAssignments:\n")

for assignment in assignments:
    print(assignment)

print("\nAgent Statistics:\n")

for agent_id, stats in agent_stats.items():
    print(agent_id, stats)

print("\nBest Agent:")
print(best_agent)

print(
    "\nreport.json generated successfully!"
)














































# import json
# import math


# # ==========================
# # LOAD INPUT DATA
# # ==========================
# file_name = input("Enter test case file: ")

# with open(file_name, "r") as file:
#     data = json.load(file)

# warehouses = data["warehouses"]
# agents = data["agents"]
# packages = data["packages"]


# # ==========================
# # DISTANCE FUNCTION
# # ==========================

# def calculate_distance(point1, point2):

#     x1 = point1[0]
#     y1 = point1[1]

#     x2 = point2[0]
#     y2 = point2[1]

#     distance = math.sqrt(
#         (x2 - x1) ** 2 +
#         (y2 - y1) ** 2
#     )

#     return distance


# # ==========================
# # AGENT STATISTICS
# # ==========================

# agent_stats = {}

# for agent in agents:

#     agent_stats[agent["id"]] = {
#         "packages_delivered": 0,
#         "total_distance": 0
#     }


# # ==========================
# # ASSIGN PACKAGES
# # ==========================

# assignments = []

# for package in packages:

#     warehouse_location = None

#     # Find warehouse location
#     for warehouse in warehouses:

#         if warehouse["id"] == package["warehouse_id"]:

#             warehouse_location = warehouse["location"]
#             break

#     # Find nearest agent
#     nearest_agent = None
#     nearest_agent_location = None
#     min_distance = float("inf")

#     for agent in agents:

#         distance = calculate_distance(
#             agent["location"],
#             warehouse_location
#         )

#         if distance < min_distance:

#             min_distance = distance
#             nearest_agent = agent["id"]
#             nearest_agent_location = agent["location"]

#     # Calculate trip distance
#     pickup_distance = calculate_distance(
#         nearest_agent_location,
#         warehouse_location
#     )

#     delivery_distance = calculate_distance(
#         warehouse_location,
#         package["destination"]
#     )

#     total_trip_distance = (
#         pickup_distance +
#         delivery_distance
#     )

#     # Save assignment
#     assignments.append({
#         "package_id": package["id"],
#         "agent_id": nearest_agent,
#         "distance": round(total_trip_distance, 2)
#     })

#     # Update statistics
#     agent_stats[nearest_agent]["packages_delivered"] += 1

#     agent_stats[nearest_agent]["total_distance"] += (
#         total_trip_distance
#     )


# # ==========================
# # ROUND TOTAL DISTANCE
# # ==========================

# for agent_id in agent_stats:

#     agent_stats[agent_id]["total_distance"] = round(
#         agent_stats[agent_id]["total_distance"],
#         2
#     )


# # ==========================
# # EFFICIENCY CALCULATION
# # ==========================

# for agent_id in agent_stats:

#     packages_delivered = (
#         agent_stats[agent_id]["packages_delivered"]
#     )

#     total_distance = (
#         agent_stats[agent_id]["total_distance"]
#     )

#     if packages_delivered > 0:

#         efficiency = (
#             total_distance /
#             packages_delivered
#         )

#     else:

#         efficiency = 0

#     agent_stats[agent_id]["efficiency"] = round(
#         efficiency,
#         2
#     )


# # ==========================
# # FIND BEST AGENT
# # ==========================

# best_agent = None
# best_efficiency = float("inf")

# for agent_id in agent_stats:

#     efficiency = (
#         agent_stats[agent_id]["efficiency"]
#     )

#     if efficiency < best_efficiency:

#         best_efficiency = efficiency
#         best_agent = agent_id


# # ==========================
# # CREATE REPORT
# # ==========================

# report = {
#     "assignments": assignments,
#     "agent_statistics": agent_stats,
#     "best_agent": best_agent
# }


# # ==========================
# # SAVE REPORT.JSON
# # ==========================

# with open("report.json", "w") as file:

#     json.dump(
#         report,
#         file,
#         indent=4
#     )


# # ==========================
# # DISPLAY RESULTS
# # ==========================

# print("\nAssignments:\n")

# for assignment in assignments:
#     print(assignment)

# print("\nAgent Statistics:\n")

# for agent_id, stats in agent_stats.items():
#     print(agent_id, stats)

# print("\nBest Agent:")
# print(best_agent)

# print("\nreport.json generated successfully!")