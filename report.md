# PulseCompanion - AI Readiness Hackathon Report
*Team name:* PulseCompanion
*Members name:* Usman Danladi Alhajji
*Solution name:* PulseCompanion - AI-Powered Heart Rate Emotional Support
*Contact details:* 2445244ksa@aou.edu.sa

## 1. Introduction
Cardiovascular health monitoring through smartwatches has become widespread, 
yet current applications are limited to fitness tracking during exercise. 
PulseCompanion addresses a critical gap: the connection between heart rate 
abnormalities and the need for immediate support — both physical and emotional.

This solution was inspired by a personal experience where elevated heart rate 
during emotional distress went unaddressed due to lack of appropriate tools. 
PulseCompanion leverages AI to bridge physical health monitoring with mental 
health support, aligned with Saudi Arabia's Vision 2030 health transformation 
goals and ITU AI Readiness framework.

## 2. Description of Use Case and Gaps in Existing Solutions

*Problem:* Most smartwatch users rely on heart rate monitoring only during 
exercise, unaware that abnormal heart rate — both high and low — can indicate 
serious health or emotional conditions requiring immediate attention.

*Existing gaps:*
- Current apps display numbers without context or support
- No connection between heart rate abnormalities and emotional or mental health
- No immediate AI-driven intervention when abnormal readings occur
- No detection or support for low heart rate (Bradycardia)
- Limited awareness of smartwatch capabilities beyond fitness tracking

*Our Solution:* PulseCompanion detects abnormal heart rate readings — both 
high and low — and initiates an AI conversation to understand the cause, 
then provides:
- Breathing exercises for stress reduction
- Emotional support and mental health guidance
- Medical consultation recommendations when needed
- Emergency alerts for critically high or low heart rates
- Policy-informed responses based on Saudi AI health frameworks

*Bradycardia Detection:*
PulseCompanion also detects critically low heart rates:
- Below 40 BPM: Emergency alert to call emergency services immediately
- Below 60 BPM: Bradycardia warning with AI conversation asking about 
  symptoms like dizziness, fatigue, or fainting, and recommending 
  immediate medical consultation

This feature was added in response to real-world cases where sudden cardiac 
events caused by low heart rate went undetected, highlighting the need for 
proactive monitoring beyond fitness tracking.

## 3. Mapped Documents (ITU-T Y.3172 Pipeline)

| Node | Use Case | Documents |
|------|----------|-----------|
| SRC | Smartwatch/smartphone heart rate sensor | Saudi Digital Health Strategy, MOH Guidelines |
| C | Mobile application processing layer | SDAIA AI Adoption Framework 2025 |
| PP | Data preprocessing and validation | Saudi Data Governance Framework |
| M | Gemini AI model for conversation analysis | SDAIA AI Ethics Guidelines |
| P | AI response with human oversight option | Saudi National AI Strategy |
| D | Cloud-based analytics and logging | Vision 2030 Health Transformation |
| SINK | User interface - chat support system | MOH Digital Health Standards |

## 4. Evaluation Scenarios

*Scenario 1 - Normal Operation (High Heart Rate):*
User detects heart rate of 120 BPM while stressed after an argument.
PulseCompanion initiates conversation, identifies emotional cause, 
provides breathing exercises. Heart rate returns to normal.

*Scenario 2 - Emergency Detection (High):*
User heart rate exceeds 150 BPM. PulseCompanion immediately displays 
emergency alert and directs user to call emergency services.

*Scenario 3 - Bradycardia Detection (Low Heart Rate):*
User heart rate drops to 50 BPM. PulseCompanion detects low heart rate,
initiates AI conversation asking about dizziness or fatigue symptoms,
and recommends immediate medical consultation. If below 40 BPM,
emergency alert is triggered immediately.

*Scenario 4 - Controversy/Privacy Concern:*
Users concerned about health data privacy. PulseCompanion addresses this 
through local processing, no data storage, and alignment with Saudi 
Personal Data Protection Law (PDPL).

## 5. Knowledge Base Sources

1. SDAIA AI Adoption Framework 2025
   - https://sdaia.gov.sa/en/SDAIA/about/Files/AIAdoptionFramework.pdf

2. Saudi National Data & AI Strategy
   - https://sdaia.gov.sa/en/SDAIA/SdaiaStrategies/Pages/NationalStrategyForDataAndAI.aspx

3. Vision 2030 Health Sector Transformation
   - https://www.vision2030.gov.sa/en/explore/programs/health-sector-transformation-program

4. Saudi AI Regulation - National Portal
   - https://my.gov.sa/en/content/109729

5. SDAIA Artificial Intelligence Authority
   - https://sdaia.gov.sa/en/SDAIA/about/Pages/AboutAI.aspx

## 6. Demo Video
YouTube Link:https://youtu.be/8f7132js09I?si=OXimX1-Rn9uqo6tb

## 7. Future Work

### Integration with Sehhaty App
PulseCompanion can be integrated with Saudi Arabia's 
official Sehhaty app to create a comprehensive health 
monitoring ecosystem benefiting both patients and doctors:

*For Patients:*
- Heart rate history and emotional health records stored securely
- AI conversation summaries shared with family doctor
- Continuous monitoring between doctor visits

*For Family Doctors:*
- Access to real heart rate readings over time
- Review of AI conversation history to understand patient patterns
- Data-driven decisions based on actual measurements
- Better diagnosis through longitudinal health data

### Expanded Vital Signs Monitoring
Beyond heart rate, PulseCompanion can monitor additional 
vital signs through smart devices:

- *Blood Pressure:* Continuous monitoring for hypertension 
  patients with AI alerts when readings are abnormal
- *Blood Sugar:* Integration with glucose monitors for 
  diabetes patients, tracking patterns over time
- *All data shared with Sehhaty App* for family doctors 
  to access real measurements over specific time periods

This transforms PulseCompanion into a comprehensive AI 
health companion, enabling doctors to make data-driven 
decisions based on actual patient vitals rather than 
single clinic visits, directly supporting Saudi Vision 2030 
goal of shifting from disease treatment to preventive 
healthcare through digital technology.