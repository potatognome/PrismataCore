# KADD Layer-Based Agent Orchestration Guide

**Strategy:** 5-Agent Layer-Based Decomposition  
**Status:** Active  
**Created:** 2026-11-11  
**Last Updated:** 2026-11-13
**Version:** 1.0.0
**Next Review By:** 2026-12-11

---

## Purpose

This guide documents the orchestration strategy for KADD (Knowledge Architecture Documentation Discipline) reviews using a 5-agent layer-based decomposition approach.

The strategy replaces the monolithic comprehensive agent with specialized agents that analyze bounded KADD layers, reducing context window pressure while maintaining comprehensive analysis coverage.

---

## Core Strategy

### Principle
- One agent per analysis focus area
- Each agent reads ALL KAD files for context
- All KAD files remain read-only
- All recommendations proposal-based
- All reports timestamped
- Sequential agent flow with consolidation

### Benefits
✅ Reduced context pressure per agent  
✅ Specialized analysis focus per agent  
✅ Clear agent responsibilities  
✅ Parallel execution opportunities  
✅ Modular, maintainable approach  
✅ Complete coverage maintained  

---

## Agent Definitions

### Agent 1: Foundation Analysis (Layers 1-2)
**File:** `.github/agents/kadd-layer-1-2-foundation-agent.md`

**Scope:**
- Layer 1: Vision, mission, concepts, foundational narratives
- Layer 2: Systems, subsystems, relationships, decisions

**Output:** kadd-foundation-analysis_YYYY-MM-DD_HHMMSS.md

**Analysis:** Concept maturity, architectural coherence, foundation health

---

### Agent 2: Execution Analysis (Layers 3-4)
**File:** `.github/agents/kadd-layer-3-4-execution-agent.md`

**Scope:**
- Layer 3: Requirements, risks, roadmap
- Layer 4: Interfaces, data models, storage, configuration, development

**Output:** kadd-execution-analysis_YYYY-MM-DD_HHMMSS.md

**Analysis:** Implementation readiness, requirements traceability, execution health

---

### Agent 3: Knowledge Capture & Reference (Layers 5 & 9)
**File:** `.github/agents/kadd-layer-5-9-knowledge-agent.md`

**Scope:**
- Layer 5: Research, lessons learned, retrospectives
- Layer 9: Glossary, appendices, references

**Output:** kadd-knowledge-analysis_YYYY-MM-DD_HHMMSS.md

**Analysis:** Glossary completeness, terminology consistency, knowledge graph readiness

---

### Agent 4: Integrity & Cohesion Analysis (Cross-Layer)
**File:** `.github/agents/kadd-layer-4-integrity-cohesion-agent.md`

**Scope:**
- All layers (reads Agents 1-3 outputs + all KAD files)
- Cross-layer integrity verification
- Architectural cohesion assessment
- Holistic KADD health evaluation

**Output:** kadd-integrity-cohesion-analysis_YYYY-MM-DD_HHMMSS.md

**Analysis:** Architectural cohesion, concept viability, cost efficiency, cross-layer risks

---

### Agent 5: Final Report Generation (Consolidation)
**File:** `.github/agents/kadd-layer-5-final-report-agent.md`

**Scope:**
- All agents (reads Agents 1-4 outputs + all KAD files)
- Comprehensive synthesis and consolidation
- Final scoring and ranking
- Executable recommendations

**Output:** kadd-review-report_YYYY-MM-DD_HHMMSS.md (FINAL, 40-50 KB)

**Analysis:** Comprehensive assessment, integrated scoring, Top 10 lists, change proposals

---

## Execution Flow

### Sequential Flow (Default)

```
Agent 1 → Agent 2 → Agent 3 → Agent 4 → Agent 5
Foundation  Execution  Knowledge  Integrity   Final
Analysis    Analysis   Analysis   Analysis    Report
 (1-2)       (3-4)     (5,9)     (Cross)  (Synthesis)
15-20KB    15-20KB   12-18KB   18-25KB   40-50KB
```

### Timeline
1. Agent 1 invoked: Foundation Analysis completes
2. Agent 2 invoked: Execution Analysis completes
3. Agent 3 invoked: Knowledge Analysis completes
4. Agent 4 invoked: Integrity Analysis completes (reads 1-3 outputs)
5. Agent 5 invoked: Final Report completes (reads 1-4 outputs)

### Execution Time
- Per Agent: 60-90 seconds average
- Total Sequence: 5-8 minutes
- Final Report Timestamp: Time Agent 5 completes

---

## Change Request Process

### How to Submit Change Requests

1. **Use Template:** `.github/kad-change-proposal.template.md`
2. **Create File:** `.github/.agent-reports/kadd/change-request_[desc]_YYYY-MM-DD.md`
3. **Complete:** All required fields in template
4. **Submit:** For Principal review and approval

### Change Request Format
- **Finding:** What was discovered
- **Rationale:** Why change is needed
- **Suggested Change:** Exact proposed modification
- **Impact Assessment:** Risks, benefits, dependencies
- **Status:** Draft → Proposed → Approved → Implemented

### Approval Process
1. Submit completed change request
2. Principal reviews and approves
3. Implementation executed
4. KAD file updated with new version
5. Change recorded in document version history

---

## Important Constraints

### Read-Only Policy
✅ All agents **READ** all KAD files  
❌ No agent **MODIFIES** any KAD file  
❌ No agent **REWRITES** KAD content  

**Rationale:** KAD files are author-owned formal concept documents

### Proposal-Based Recommendations
✅ All recommendations go through change-request process  
✅ Formal proposal format required  
✅ Principal approval required  

**Rationale:** Ensures author intent is preserved

### All Reports Timestamped
✅ Every agent report includes datetime in filename  
✅ Datetime format: YYYY-MM-DD_HHMMSS  

**Rationale:** Enables tracking over time

### All Reports Read-Only
✅ Reports are analytical documents  
✅ Reports contain findings and recommendations  
❌ Reports do not modify canonical documents  

**Rationale:** Maintains separation between analysis and implementation

---

## Quality Standards

### Report Quality
- Comprehensive analysis of assigned scope
- Specific, actionable findings
- Clear justifications and rationales
- Proposal-based recommendations
- Professional, clear writing
- Proper citation of source documents

### Analysis Rigor
- All KAD documents read and considered
- Context from other layers understood
- Findings traced to sources
- Alternative approaches considered
- Edge cases identified
- Trade-offs analyzed

### Scoring Accuracy
- 8 numerical scores provided per agent
- Scores justify findings
- Scores consistent across reports
- Aggregate calculation transparent
- Scoring methodology documented

---

## Recommended Review Cadence

### Full Comprehensive Review
- **Frequency:** Quarterly or on major changes
- **Triggers:** Major feature completion, architectural changes, integration of new layers

### Targeted Reviews
- **Frequency:** As-needed
- **Scope:** Specific layers or documents

### Continuous Monitoring
- **Frequency:** Ongoing
- **Method:** Manual review and change requests

---

## References

### Agent Definitions
- kadd-layer-1-2-foundation-agent.md
- kadd-layer-3-4-execution-agent.md
- kadd-layer-5-9-knowledge-agent.md
- kadd-layer-4-integrity-cohesion-agent.md
- kadd-layer-5-final-report-agent.md

### Process Templates
- change-proposal-template.md

### Output Location
- .github/.agent-reports/kadd/ - All agent reports

---

## Final Principles

1. **Knowledge First:** KADD is the authoritative knowledge base
2. **Read-Only Analysis:** Agents analyze but never modify
3. **Proposal-Based:** All changes proposed, not mandated
4. **Author Protected:** KAD author's intent is preserved
5. **Timestamped:** All work is dated and tracked
6. **Comprehensive:** All layers reviewed on each assessment
7. **Sequential:** Clear flow from analysis to synthesis to action
8. **Transparent:** Process is clear and documented

---

**Last Updated:** 2026-11-11  
**Next Review:** 2026-11-18 or upon major changes
