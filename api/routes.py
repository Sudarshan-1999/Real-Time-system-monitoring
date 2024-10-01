from flask import jsonify,json
from utils.check_system import check_system_health, check_system_uptime
from automation.system_monitoring import check_disk_space
def setup_routes(app):
    @app.route('/api/status', methods=['GET'])
    def get_status():
        """Returns the status of the API."""
        return jsonify({"status": "API is running", "version": "1.0.0"})

    @app.route('/api/health', methods=['GET'])
    def get_health():
        """Returns system health check."""
        # For simplicity, it returns a static value, but you can add real checks.
        uptime = check_system_uptime()
        json_load_uptime = json.loads(uptime)
        health = check_system_health()

        return jsonify({"health": health, "uptime": json_load_uptime })
    
    @app.route("/api/diskusage" , methods=["GET"])
    def get_usage():
        disk_check = check_disk_space() 
        return disk_check