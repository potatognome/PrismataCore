# KADD Layer-Based Agent Orchestration Guide

**Established:** 2026-11-11  
**Strategy:** 5-Agent Layer-Based Decomposition  
**Status:** Active  

---

## Purpose

This guide documents the orchestration strategy for KADD (Knowledge Architecture Documentation Discipline) reviews using a 5-agent layer-based decomposition approach.

The strategy replaces the monolithic comprehensive agent with specialized agents that analyze bounded KADD layers, reducing context window pressure while maintaining comprehensive analysis coverage.

---

## Core Strategy

### Principle
- **One agent per analysis focus area**
- **Each agent reads ALL KAD files for context**
- **All KAD files remain read-only**
- **All recommendations proposal-based**
- **All reports timestamped**
- **Sequential agent flow with consolidation**

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

**Output:**
- `kadd-foundation-analysis_YYYY-MM-DD_HHMMSS.md`
- Concept maturity assessment
- Architectural coherence findings
- 8 numerical scores
- Foundation health summary

**Analysis Tasks:**
1. Vision clarity assessment
2. Concept analysis and maturity
3. Foundational narratives validation
4. System architecture assessment
5. Relationship integrity verification
6. Architectural decision quality assessment

---

### Agent 2: Execution Analysis (Layers 3-4)
**File:** `.github/agents/kadd-layer-3-4-execution-agent.md`

**Scope:**
- Layer 3: Requirements, risks, roadmap
- Layer 4: Interfaces, data models, storage, configuration, development

**Output:**
- `kadd-execution-analysis_YYYY-MM-DD_HHMMSS.md`
- Implementation readiness assessment
- Requirements traceability findings
- 8 numerical scores
- Execution health summary

**Analysis Tasks:**
1. Requirements completeness and traceability
2. Risk identification and mitigation assessment
3. Roadmap viability evaluation
4. Interface design assessment
5. Data model quality evaluation
6. Implementation readiness assessment

---

### Agent 3: Knowledge Capture & Reference (Layers 5 & 9)
**File:** `.github/agents/kadd-layer-5-9-knowledge-agent.md`

**Scope:**
- Layer 5: Research, lessons learned, retrospectives
- Layer 9: Glossary, appendices, references

**Output:**
- `kadd-knowledge-analysis_YYYY-MM-DD_HHMMSS.md`
- Glossary completeness assessment
- Terminology consistency analysis
- Knowledge graph readiness evaluation
- 8 numerical scores
- Knowledge system health summary

**Analysis Tasks:**
1. Research findings documentation assessment
2. Lessons learned quality evaluation
3. Glossary completeness and clarity
4. Terminology consistency analysis
5. References completeness assessment
6. Knowledge graph readiness evaluation

---

### Agent 4: Integrity & Cohesion Analysis (Cross-Layer)
**File:** `.github/agents/kadd-layer-4-integrity-cohesion-agent.md`

**Scope:**
- All layers (reads Agents 1-3 outputs + all KAD files)
- Cross-layer integrity verification
- Architectural cohesion assessment
- Holistic KADD health evaluation

**Inputs:**
- Agent 1 output report
- Agent 2 output report
- Agent 3 output report
- All KAD files

**Output:**
- `kadd-integrity-cohesion-analysis_YYYY-MM-DD_HHMMSS.md`
- Architectural cohesion findings
- Concept viability assessment
- Cost efficiency evaluation
- Knowledge graph readiness score
- Cross-layer risks and opportunities
- 8 numerical scores

**Analysis Tasks:**
1. Architectural cohesion verification
2. Vision-to-implementation alignment
3. Concept viability assessment
4. Cost efficiency analysis
5. Knowledge graph readiness evaluation
6. Ambiguity review (role, layer, concept, terminology)
7. Duplication analysis
8. Intent clarity assessment

---

### Agent 5: Final Report Generation (Consolidation)
**File:** `.github/agents/kadd-layer-5-final-report-agent.md`

**Scope:**
- All agents (reads Agents 1-4 outputs + all KAD files)
- Comprehensive synthesis and consolidation
- Final scoring and ranking
- Executable recommendations

**Inputs:**
- Agent 1 output report
- Agent 2 output report
- Agent 3 output report
- Agent 4 output report
- All KAD files

**Output:**
- `kadd-review-report_YYYY-MM-DD_HHMMSS.md` (FINAL, 40-50 KB)
- Comprehensive KADD assessment
- Integrated 8-point scoring
- Top 10 Strengths (ranked)
- Top 10 Risks (ranked)
- Top 10 Opportunities (ranked)
- Top 10 Recommended Actions (ranked)
- Change proposals formalized
- Next steps and governance

**Synthesis Tasks:**
1. Aggregate all findings from Agents 1-4
2. Identify patterns and themes
3. Calculate integrated scores
4. Generate and rank Top 10 lists
5. Formalize change proposals
6. Create comprehensive final report

---

## Execution Flow

### Sequential Flow (Default)

```
Agent 1 → Agent 2 → Agent 3 → Agent 4 → Agent 5
Foundation  Execution  Knowledge  Integrity   Final
Analysis    Analysis   Analysis   Analysis    Report
  (1-2)      (3-4)      (5,9)    (Cross)   (Synthesis)
  15-20KB    15-20KB    12-18KB   18-25KB   40-50KB
```

### Timeline
1. **Agent 1** invoked: Foundation Analysis completes
2. **Agent 2** invoked: Execution Analysis completes
3. **Agent 3** invoked: Knowledge Analysis completes
4. **Agent 4** invoked: Integrity Analysis completes (reads 1-3 outputs)
5. **Agent 5** invoked: Final Report completes (reads 1-4 outputs)

### Execution Time
- **Per Agent:** 60-90 seconds average
- **Total Sequence:** 5-8 minutes
- **Final Report Timestamp:** Time Agent 5 completes

---

## How to Invoke Agents

### Invoke Agent 1: Foundation Analysis
```
task:
  agent_type: general-purpose
  name: kadd-foundation-analysis
  prompt: |
    You are a KADD-aware Foundation Analysis Agent.
    
    Read the agent definition at:
    .github/agents/kadd-layer-1-2-foundation-agent.md
    
    Execute the complete Foundation Analysis for PrismataCore KADD.
    
    Output location: .github/.agent-reports/kadd/
    Filename format: kadd-foundation-analysis_YYYY-MM-DD_HHMMSS.md
```

### Invoke Agent 2: Execution Analysis
```
task:
  agent_type: general-purpose
  name: kadd-execution-analysis
  prompt: |
    You are a KADD-aware Execution Analysis Agent.
    
    Read the agent definition at:
    .github/agents/kadd-layer-3-4-execution-agent.md
    
    Execute the complete Execution Analysis for PrismataCore KADD.
    
    Output location: .github/.agent-reports/kadd/
    Filename format: kadd-execution-analysis_YYYY-MM-DD_HHMMSS.md
```

### Invoke Agent 3: Knowledge Analysis
```
task:
  agent_type: general-purpose
  name: kadd-knowledge-analysis
  prompt: |
    You are a KADD-aware Knowledge Analysis Agent.
    
    Read the agent definition at:
    .github/agents/kadd-layer-5-9-knowledge-agent.md
    
    Execute the complete Knowledge Capture & Reference Analysis for PrismataCore KADD.
    
    Output location: .github/.agent-reports/kadd/
    Filename format: kadd-knowledge-analysis_YYYY-MM-DD_HHMMSS.md
```

### Invoke Agent 4: Integrity & Cohesion Analysis
```
task:
  agent_type: general-purpose
  name: kadd-integrity-cohesion-analysis
  prompt: |
    You are a KADD-aware Integrity & Cohesion Analysis Agent.
    
    Read the agent definition at:
    .github/agents/kadd-layer-4-integrity-cohesion-agent.md
    
    REQUIRED INPUTS:
    Read and consume the following agent reports (in order):
    1. .github/.agent-reports/kadd/kadd-foundation-analysis_[timestamp].md
    2. .github/.agent-reports/kadd/kadd-execution-analysis_[timestamp].md
    3. .github/.agent-reports/kadd/kadd-knowledge-analysis_[timestamp].md
    
    Execute the complete Cross-Layer Integrity & Cohesion Analysis.
    
    Output location: .github/.agent-reports/kadd/
    Filename format: kadd-integrity-cohesion-analysis_YYYY-MM-DD_HHMMSS.md
```

### Invoke Agent 5: Final Report Generation
```
task:
  agent_type: general-purpose
  name: kadd-final-report
  prompt: |
    You are a KADD-aware Final Report Generation Agent.
    
    Read the agent definition at:
    .github/agents/kadd-layer-5-final-report-agent.md
    
    REQUIRED INPUTS:
    Read and consume all four specialized agent reports:
    1. .github/.agent-reports/kadd/kadd-foundation-analysis_[timestamp].md
    2. .github/.agent-reports/kadd/kadd-execution-analysis_[timestamp].md
    3. .github/.agent-reports/kadd/kadd-knowledge-analysis_[timestamp].md
    4. .github/.agent-reports/kadd/kadd-integrity-cohesion-analysis_[timestamp].md
    
    Execute comprehensive synthesis and generate final consolidated report.
    
    Output location: .github/.agent-reports/kadd/
    Filename format: kadd-review-report_YYYY-MM-DD_HHMMSS.md
    Status: FINAL
```

---

## Change Request Process

### How to Submit Change Requests

1. **Use Template:** `.github/change-proposal-template.md`
2. **Create File:** `.github/.agent-reports/kadd/change-request_[description]_YYYY-MM-DD.md`
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
3. Implementation executed (by Principal or delegate)
4. KAD file updated with new version
5. Change recorded in document version history

---

## Important Constraints

### Read-Only Policy
✅ All agents **READ** all KAD files  
❌ No agent **MODIFIES** any KAD file  
❌ No agent **REWRITES** KAD content  
❌ No agent **REFACTORS** KAD structure  

**Rationale:** KAD files are author-owned formal concept documents protected under KADD author's notes protection policy.

### Proposal-Based Recommendations
✅ All recommendations go through change-request process  
✅ Formal proposal format required  
✅ Principal approval required  
❌ No direct KAD modifications  

**Rationale:** Ensures author intent is preserved and all changes are explicitly approved.

### All Reports Timestamped
✅ Every agent report includes datetime in filename  
✅ Datetime format: `YYYY-MM-DD_HHMMSS`  
✅ Example: `kadd-review-report_2026-11-11_180000.md`  

**Rationale:** Enables tracking of analysis over time and prevents confusion between reports.

### All Reports Read-Only
✅ Reports are analytical documents  
✅ Reports contain findings and recommendations  
✅ Reports do not modify canonical documents  
❌ Reports are not implementation artifacts  

**Rationale:** Maintains clear separation between analysis and implementation.

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

## Maintenance & Evolution

### Agent Updates
- Agent definitions may be updated to improve analysis
- Updates recorded in agent file with change date
- All agents maintain backward compatibility
- Version history preserved

### Process Improvements
- Lessons learned captured from each review
- Process optimizations identified
- Agent definitions refined based on experience
- Orchestration guide updated

### Governance
- Principal owns all KADD content
- Agents operate under Principal's authority
- Recommendations require Principal approval
- Implementation controlled by Principal

---

## Recommended Review Cadence

### Full Comprehensive Review
- **Frequency:** Quarterly or on major changes
- **Triggers:**
  - Major feature completion
  - Significant architectural changes
  - Integration of new layers
  - Principal-requested assessment

### Targeted Reviews
- **Frequency:** As-needed
- **Scope:** Specific layers or documents
- **Use:** For focused analysis of particular areas

### Continuous Monitoring
- **Frequency:** Ongoing
- **Method:** Manual review and change requests
- **Use:** Incremental improvements between full reviews

---

## Success Metrics

### Report Quality
- Findings are specific and actionable
- Recommendations are proposal-based
- Analysis is comprehensive
- Scoring is accurate and justified

### Process Efficiency
- Agent execution completes in expected timeframe
- Context window pressure manageable per agent
- Output quality maintained across agents
- Consolidation successful and complete

### Knowledge Preservation
- Author intent preserved
- KAD files unmodified
- Change process respected
- Historical record maintained

### User Satisfaction
- Reports provide valuable insights
- Recommendations are useful
- Process is clear and transparent
- Governance is effective

---

## References

### Agent Definitions
- `kadd-layer-1-2-foundation-agent.md`
- `kadd-layer-3-4-execution-agent.md`
- `kadd-layer-5-9-knowledge-agent.md`
- `kadd-layer-4-integrity-cohesion-agent.md`
- `kadd-layer-5-final-report-agent.md`

### Process Templates
- `change-proposal-template.md`

### KADD Documentation
- `canonical/kadd/` - All KAD documents
- `canonical/kadd/1-definitions/` - Layer 1
- `canonical/kadd/2-architecture/` - Layer 2
- `canonical/kadd/3-planning/` - Layer 3
- `canonical/kadd/4-implementation/` - Layer 4
- `canonical/kadd/5-post-implementation/` - Layer 5
- `canonical/kadd/9-reference/` - Layer 9

### Output Location
- `.github/.agent-reports/kadd/` - All agent reports

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
