#!/usr/bin/env python3
"""
GitHub Statistics Collector for AXL Lab
Pulls repository and contribution statistics to measure vibe coding impact
"""

import os
import json
import requests
from datetime import datetime, timedelta
from collections import defaultdict
import argparse
import time

class GitHubStatsCollector:
    def __init__(self, token, org_name="axl-lab"):
        self.token = token
        self.org_name = org_name
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = "https://api.github.com"
        
    def get_organization_info(self):
        """Get basic organization information"""
        url = f"{self.base_url}/orgs/{self.org_name}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_repositories(self):
        """Get all repositories for the organization"""
        repos = []
        page = 1
        
        while True:
            url = f"{self.base_url}/orgs/{self.org_name}/repos?page={page}&per_page=100"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data:
                break
                
            repos.extend(data)
            page += 1
            
        return repos
    
    def get_pull_requests(self, repo_name, state="all"):
        """Get pull requests for a repository"""
        prs = []
        page = 1
        
        while True:
            url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/pulls?state={state}&page={page}&per_page=100"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data:
                break
                
            prs.extend(data)
            page += 1
            
        return prs
    
    def get_commits(self, repo_name, since=None):
        """Get commits for a repository"""
        commits = []
        page = 1
        
        params = {"per_page": 100}
        if since:
            params["since"] = since.isoformat()
        
        while True:
            url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/commits"
            response = requests.get(url, headers=self.headers, params={**params, "page": page})
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data:
                break
                
            commits.extend(data)
            page += 1
            
        return commits
    
    def get_commit_details(self, repo_name, commit_sha):
        """Get detailed information about a specific commit including changes"""
        url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/commits/{commit_sha}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return None
    
    def get_code_frequency(self, repo_name):
        """Get code frequency statistics (additions/deletions over time)"""
        url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/stats/code_frequency"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return []
    
    def get_contributors(self, repo_name):
        """Get contributors statistics for a repository"""
        url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/stats/contributors"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return []
    
    def get_languages(self, repo_name):
        """Get language breakdown for a repository"""
        url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/languages"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return {}
    
    def get_workflows(self, repo_name):
        """Get workflows for a repository"""
        workflows = []
        page = 1
        
        while True:
            url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/actions/workflows?page={page}&per_page=100"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data.get("workflows"):
                break
                
            workflows.extend(data["workflows"])
            page += 1
            
        return workflows
    
    def get_workflow_runs(self, repo_name, workflow_id=None, since=None):
        """Get workflow runs for a repository or specific workflow"""
        runs = []
        page = 1
        
        # Build URL based on whether we're getting runs for a specific workflow
        if workflow_id:
            base_url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/actions/workflows/{workflow_id}/runs"
        else:
            base_url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/actions/runs"
        
        params = {"per_page": 100}
        if since:
            params["created"] = f">={since.strftime('%Y-%m-%d')}"
        
        while True:
            response = requests.get(base_url, headers=self.headers, params={**params, "page": page})
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data.get("workflow_runs"):
                break
                
            runs.extend(data["workflow_runs"])
            page += 1
            
        return runs
    
    def get_workflow_run_jobs(self, repo_name, run_id):
        """Get jobs for a specific workflow run"""
        jobs = []
        page = 1
        
        while True:
            url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/actions/runs/{run_id}/jobs?page={page}&per_page=100"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code != 200:
                break
                
            data = response.json()
            if not data.get("jobs"):
                break
                
            jobs.extend(data["jobs"])
            page += 1
            
        return jobs
    
    def get_workflow_usage(self, repo_name, workflow_id):
        """Get billable usage for a specific workflow"""
        url = f"{self.base_url}/repos/{self.org_name}/{repo_name}/actions/workflows/{workflow_id}/timing"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return {}
    
    def calculate_stats(self, since_days=90):
        """Calculate comprehensive statistics for the organization"""
        since_date = datetime.now() - timedelta(days=since_days)
        
        stats = {
            "organization": self.org_name,
            "generated_at": datetime.now().isoformat(),
            "period_days": since_days,
            "repositories": {
                "total": 0,
                "active": 0,
                "languages": defaultdict(int)
            },
            "pull_requests": {
                "total": 0,
                "open": 0,
                "closed": 0,
                "merged": 0,
                "average_time_to_merge_hours": 0,
                "by_month": defaultdict(int)
            },
            "commits": {
                "total": 0,
                "by_author": defaultdict(int),
                "by_month": defaultdict(int)
            },
            "code_changes": {
                "total_additions": 0,
                "total_deletions": 0,
                "net_lines": 0,
                "by_repo": {}
            },
            "contributors": {
                "total": set(),
                "active_last_30_days": set(),
                "by_repo": {}
            },
            "activity_metrics": {
                "commits_per_pr": 0,
                "lines_per_commit": 0,
                "pr_velocity": 0  # PRs per week
            },
            "github_actions": {
                "total_workflows": 0,
                "active_workflows": 0,
                "total_runs": 0,
                "successful_runs": 0,
                "failed_runs": 0,
                "cancelled_runs": 0,
                "average_duration_minutes": 0,
                "total_duration_minutes": 0,
                "by_status": defaultdict(int),
                "by_workflow": {},
                "by_month": defaultdict(int),
                "top_workflows": [],
                "failure_rate": 0,
                "success_rate": 0
            }
        }
        
        # Get all repositories
        repos = self.get_repositories()
        stats["repositories"]["total"] = len(repos)
        
        merge_times = []
        
        for idx, repo in enumerate(repos, 1):
            repo_name = repo["name"]
            print(f"Processing repository {idx}/{len(repos)}: {repo_name}")
            
            # Check if repo is active (has commits in the period)
            commits = self.get_commits(repo_name, since=since_date)
            print(f"  Found {len(commits)} commits")
            if commits:
                stats["repositories"]["active"] += 1
            
            # Get languages
            languages = self.get_languages(repo_name)
            for lang, bytes_count in languages.items():
                stats["repositories"]["languages"][lang] += bytes_count
            
            # Get pull requests
            prs = self.get_pull_requests(repo_name)
            for pr in prs:
                created_date = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                
                if created_date >= since_date:
                    stats["pull_requests"]["total"] += 1
                    month_key = created_date.strftime("%Y-%m")
                    stats["pull_requests"]["by_month"][month_key] += 1
                    
                    if pr["state"] == "open":
                        stats["pull_requests"]["open"] += 1
                    else:
                        stats["pull_requests"]["closed"] += 1
                        
                        if pr.get("merged_at"):
                            stats["pull_requests"]["merged"] += 1
                            merged_date = datetime.strptime(pr["merged_at"], "%Y-%m-%dT%H:%M:%SZ")
                            merge_time = (merged_date - created_date).total_seconds() / 3600
                            merge_times.append(merge_time)
            
            # Get GitHub Actions data
            print(f"  Processing GitHub Actions...")
            workflows = self.get_workflows(repo_name)
            stats["github_actions"]["total_workflows"] += len(workflows)
            
            # Get workflow runs for this repository
            workflow_runs = self.get_workflow_runs(repo_name, since=since_date)
            
            workflow_durations = []
            for run in workflow_runs:
                run_date = datetime.strptime(run["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                if run_date >= since_date:
                    stats["github_actions"]["total_runs"] += 1
                    
                    # Track by month
                    month_key = run_date.strftime("%Y-%m")
                    stats["github_actions"]["by_month"][month_key] += 1
                    
                    # Track by status
                    status = run["status"]
                    conclusion = run.get("conclusion", "in_progress")
                    stats["github_actions"]["by_status"][conclusion] += 1
                    
                    if conclusion == "success":
                        stats["github_actions"]["successful_runs"] += 1
                    elif conclusion == "failure":
                        stats["github_actions"]["failed_runs"] += 1
                    elif conclusion == "cancelled":
                        stats["github_actions"]["cancelled_runs"] += 1
                    
                    # Calculate duration if run is completed
                    if run.get("updated_at") and status == "completed":
                        start_time = datetime.strptime(run["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                        end_time = datetime.strptime(run["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
                        duration_minutes = (end_time - start_time).total_seconds() / 60
                        workflow_durations.append(duration_minutes)
                        stats["github_actions"]["total_duration_minutes"] += duration_minutes
                    
                    # Track by workflow
                    workflow_name = run["name"]
                    if workflow_name not in stats["github_actions"]["by_workflow"]:
                        stats["github_actions"]["by_workflow"][workflow_name] = {
                            "runs": 0,
                            "success": 0,
                            "failure": 0,
                            "cancelled": 0,
                            "total_duration": 0
                        }
                    
                    stats["github_actions"]["by_workflow"][workflow_name]["runs"] += 1
                    if conclusion == "success":
                        stats["github_actions"]["by_workflow"][workflow_name]["success"] += 1
                    elif conclusion == "failure":
                        stats["github_actions"]["by_workflow"][workflow_name]["failure"] += 1
                    elif conclusion == "cancelled":
                        stats["github_actions"]["by_workflow"][workflow_name]["cancelled"] += 1
                    
                    if run.get("updated_at") and status == "completed":
                        stats["github_actions"]["by_workflow"][workflow_name]["total_duration"] += duration_minutes
            
            # Count active workflows (those with recent runs)
            if workflow_runs:
                stats["github_actions"]["active_workflows"] += len(set(run["name"] for run in workflow_runs))
            
            # Process commits
            repo_additions = 0
            repo_deletions = 0
            
            for commit in commits:
                commit_date = datetime.strptime(commit["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
                month_key = commit_date.strftime("%Y-%m")
                
                stats["commits"]["total"] += 1
                stats["commits"]["by_month"][month_key] += 1
                
                author = commit["commit"]["author"]["name"]
                stats["commits"]["by_author"][author] += 1
                stats["contributors"]["total"].add(author)
                
                # Check if active in last 30 days
                if commit_date >= datetime.now() - timedelta(days=30):
                    stats["contributors"]["active_last_30_days"].add(author)
                
                # Get detailed commit information for code changes
                # Note: This makes an API call per commit, so we'll sample for large repos
                if len(commits) <= 100 or (len(commits) > 100 and hash(commit["sha"]) % 10 == 0):
                    commit_details = self.get_commit_details(repo_name, commit["sha"])
                    if commit_details and "stats" in commit_details:
                        additions = commit_details["stats"].get("additions", 0)
                        deletions = commit_details["stats"].get("deletions", 0)
                        
                        # If we're sampling, multiply by sampling rate
                        if len(commits) > 100:
                            additions *= 10
                            deletions *= 10
                        
                        repo_additions += additions
                        repo_deletions += deletions
                        stats["code_changes"]["total_additions"] += additions
                        stats["code_changes"]["total_deletions"] += deletions
                    
                    # Rate limit handling
                    time.sleep(0.1)  # Small delay to avoid hitting rate limits
            
            # If commit details didn't work, try code frequency as fallback
            if repo_additions == 0 and repo_deletions == 0:
                code_freq = self.get_code_frequency(repo_name)
                
                for week_data in code_freq:
                    if len(week_data) >= 3:
                        timestamp = week_data[0]
                        week_date = datetime.fromtimestamp(timestamp)
                        
                        if week_date >= since_date:
                            additions = week_data[1]
                            deletions = abs(week_data[2])
                            
                            repo_additions += additions
                            repo_deletions += deletions
                            stats["code_changes"]["total_additions"] += additions
                            stats["code_changes"]["total_deletions"] += deletions
            
            stats["code_changes"]["by_repo"][repo_name] = {
                "additions": repo_additions,
                "deletions": repo_deletions,
                "net": repo_additions - repo_deletions
            }
        
        # Calculate derived metrics
        stats["code_changes"]["net_lines"] = stats["code_changes"]["total_additions"] - stats["code_changes"]["total_deletions"]
        
        if merge_times:
            stats["pull_requests"]["average_time_to_merge_hours"] = sum(merge_times) / len(merge_times)
        
        if stats["pull_requests"]["total"] > 0:
            stats["activity_metrics"]["commits_per_pr"] = stats["commits"]["total"] / stats["pull_requests"]["total"]
        
        if stats["commits"]["total"] > 0:
            total_changes = stats["code_changes"]["total_additions"] + stats["code_changes"]["total_deletions"]
            stats["activity_metrics"]["lines_per_commit"] = total_changes / stats["commits"]["total"]
        
        weeks_in_period = since_days / 7
        stats["activity_metrics"]["pr_velocity"] = stats["pull_requests"]["total"] / weeks_in_period
        
        # Calculate GitHub Actions metrics
        if stats["github_actions"]["total_runs"] > 0:
            stats["github_actions"]["average_duration_minutes"] = (
                stats["github_actions"]["total_duration_minutes"] / stats["github_actions"]["total_runs"]
            )
            stats["github_actions"]["success_rate"] = (
                stats["github_actions"]["successful_runs"] / stats["github_actions"]["total_runs"] * 100
            )
            stats["github_actions"]["failure_rate"] = (
                stats["github_actions"]["failed_runs"] / stats["github_actions"]["total_runs"] * 100
            )
        
        # Find top workflows by run count
        if stats["github_actions"]["by_workflow"]:
            top_workflows = sorted(
                stats["github_actions"]["by_workflow"].items(),
                key=lambda x: x[1]["runs"],
                reverse=True
            )[:5]
            stats["github_actions"]["top_workflows"] = [
                {
                    "name": name,
                    "runs": data["runs"],
                    "success_rate": (data["success"] / data["runs"] * 100) if data["runs"] > 0 else 0,
                    "avg_duration": (data["total_duration"] / data["runs"]) if data["runs"] > 0 else 0
                }
                for name, data in top_workflows
            ]
        
        # Convert sets to lists for JSON serialization
        stats["contributors"]["total"] = len(stats["contributors"]["total"])
        stats["contributors"]["active_last_30_days"] = len(stats["contributors"]["active_last_30_days"])
        
        # Convert defaultdicts to regular dicts
        stats["repositories"]["languages"] = dict(stats["repositories"]["languages"])
        stats["pull_requests"]["by_month"] = dict(stats["pull_requests"]["by_month"])
        stats["commits"]["by_month"] = dict(stats["commits"]["by_month"])
        stats["commits"]["by_author"] = dict(stats["commits"]["by_author"])
        stats["github_actions"]["by_status"] = dict(stats["github_actions"]["by_status"])
        stats["github_actions"]["by_month"] = dict(stats["github_actions"]["by_month"])
        
        return stats
    
    def generate_summary_report(self, stats):
        """Generate a human-readable summary report"""
        report = f"""
# GitHub Statistics Report for {stats['organization']}
Generated: {stats['generated_at']}
Period: Last {stats['period_days']} days

## Repository Overview
- Total repositories: {stats['repositories']['total']}
- Active repositories: {stats['repositories']['active']}
- Top languages: {', '.join(sorted(stats['repositories']['languages'].keys(), 
                                    key=lambda x: stats['repositories']['languages'][x], 
                                    reverse=True)[:5])}

## Pull Request Activity
- Total PRs: {stats['pull_requests']['total']}
- Open PRs: {stats['pull_requests']['open']}
- Merged PRs: {stats['pull_requests']['merged']}
- Average time to merge: {stats['pull_requests']['average_time_to_merge_hours']:.1f} hours
- PR velocity: {stats['activity_metrics']['pr_velocity']:.1f} PRs/week

## Commit Activity
- Total commits: {stats['commits']['total']}
- Average commits per PR: {stats['activity_metrics']['commits_per_pr']:.1f}
- Top contributors: {', '.join(sorted(stats['commits']['by_author'].keys(), 
                                     key=lambda x: stats['commits']['by_author'][x], 
                                     reverse=True)[:5])}

## Code Changes
- Total additions: {stats['code_changes']['total_additions']:,} lines
- Total deletions: {stats['code_changes']['total_deletions']:,} lines
- Net change: {stats['code_changes']['net_lines']:,} lines
- Average lines per commit: {stats['activity_metrics']['lines_per_commit']:.1f}

## Team Activity
- Total contributors: {stats['contributors']['total']}
- Active in last 30 days: {stats['contributors']['active_last_30_days']}

## GitHub Actions
- Total workflows: {stats['github_actions']['total_workflows']}
- Active workflows: {stats['github_actions']['active_workflows']}
- Total runs: {stats['github_actions']['total_runs']}
- Success rate: {stats['github_actions']['success_rate']:.1f}%
- Failure rate: {stats['github_actions']['failure_rate']:.1f}%
- Average run duration: {stats['github_actions']['average_duration_minutes']:.1f} minutes
- Top workflows by usage:"""
        
        # Add top workflows if available
        if stats['github_actions'].get('top_workflows'):
            for workflow in stats['github_actions']['top_workflows']:
                report += f"\n  - {workflow['name']}: {workflow['runs']} runs, {workflow['success_rate']:.1f}% success, {workflow['avg_duration']:.1f} min avg"
        else:
            report += "\n  - No workflow data available"
        
        report += f"""

## Vibe Coding Impact Indicators
- High PR velocity ({stats['activity_metrics']['pr_velocity']:.1f} PRs/week) suggests active development
- Quick merge times ({stats['pull_requests']['average_time_to_merge_hours']:.1f} hours) indicate efficient workflow
- Active contributor base shows team engagement
- CI/CD automation with {stats['github_actions']['success_rate']:.1f}% success rate enables rapid iteration
"""
        return report

def main():
    parser = argparse.ArgumentParser(description="Collect GitHub statistics for AXL Lab")
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    parser.add_argument("--org", default="axl-lab", help="GitHub organization name")
    parser.add_argument("--days", type=int, default=90, help="Number of days to look back")
    parser.add_argument("--output", default="github_stats.json", help="Output JSON file")
    
    args = parser.parse_args()
    
    collector = GitHubStatsCollector(args.token, args.org)
    
    print(f"Collecting statistics for {args.org} over the last {args.days} days...")
    stats = collector.calculate_stats(args.days)
    
    # Save JSON data
    with open(args.output, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Statistics saved to {args.output}")
    
    # Generate and print summary report
    report = collector.generate_summary_report(stats)
    print(report)
    
    # Save report
    report_file = args.output.replace(".json", "_report.md")
    with open(report_file, "w") as f:
        f.write(report)
    print(f"Report saved to {report_file}")

if __name__ == "__main__":
    main()
