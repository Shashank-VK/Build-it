// Solo AI Product Engineering System v1.0
// AI Development Harness — ABAC Policy (CAP-25, SC-07) — FIXED per validation V-OB-3
// Valid Cedar syntax. Default-deny engine. Class-3 requires permit + approval token.

// 0. Session/role context (used by conditions below)
//    context.role: String e.g. "Coder" | "DevOps" | "Planner" | "Auditor"
//    context.has_human_approval: Bool, context.approval_token_valid: Bool

// 1. Class 0: Read-Only Actions permitted for all authenticated agents
permit(
    principal,
    action in [
        Action::"read_file",
        Action::"list_dir",
        Action::"grep_search",
        Action::"view_file",
        Action::"find_by_name",
        Action::"read_url_content",
        Action::"search_web"
    ],
    resource
);

// 2. Class 1 & 2: Sandboxed Workspace Mutations for Coding, DevOps, Planner
permit(
    principal,
    action in [
        Action::"write_to_file",
        Action::"replace_file_content",
        Action::"run_test",
        Action::"create_branch"
    ],
    resource in Directory::"workspace"
) when {
    [Role::"Coder", Role::"DevOps", Role::"Planner"].contains(principal)
};

// 3. Class 3: Irreversible actions require HUMAN APPROVAL (permit + valid token)
permit(
    principal,
    action in [
        Action::"git_push_main",
        Action::"drop_database",
        Action::"terraform_apply_production",
        Action::"publish_package"
    ],
    resource
) when {
    context.has_human_approval == true &&
    context.approval_token_valid == true
};

// 4. Class 3: Deny unless approved (defense in depth; default-deny already blocks)
forbid(
    principal,
    action in [
        Action::"git_push_main",
        Action::"drop_database",
        Action::"terraform_apply_production",
        Action::"publish_package"
    ],
    resource
) unless {
    context.has_human_approval == true &&
    context.approval_token_valid == true
};

// 5. Zero-Trust Path Boundary: no access to host-sensitive paths (absolute, no `~`)
forbid(
    principal,
    action,
    resource
) when {
    resource.path like "/etc/*" ||
    resource.path like "/root/*" ||
    resource.path like "/home/*/.ssh/*" ||
    resource.path like "/home/*/.aws/*" ||
    resource.path like "/home/*/.gnupg/*" ||
    resource.path like "/home/*/.config/gcloud/*" ||
    resource.path like "/Users/*/.ssh/*" ||
    resource.path like "/Users/*/.aws/*"
};
