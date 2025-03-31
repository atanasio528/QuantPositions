
-- Drop tables if they already exist
DROP TABLE IF EXISTS applied;
DROP TABLE IF EXISTS positions;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS users;

-- Create the users table to store user information
CREATE TABLE users (
    usrid VARCHAR(50) PRIMARY KEY, -- Unique user ID
    level VARCHAR(20) CHECK (level IN ('Intern', 'NewGrad', 'Associate', 'Senior', 'VP')), -- User's seniority level
    email VARCHAR(255) UNIQUE NOT NULL, -- User email (must be unique)
    first_name VARCHAR(100) NOT NULL, -- User's first name
    last_name VARCHAR(100) NOT NULL, -- User's last name
    school VARCHAR(100), -- User's school
    password_hash TEXT NOT NULL, -- Password (hashed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last updated timestamp
    autho VARCHAR(50) DEFAULT 'read' -- Authorization level (e.g. read, edit, admin)
);

-- Create the companies table to store company information
CREATE TABLE companies (
    cpid VARCHAR(50) PRIMARY KEY, -- Unique company ID
    cpname VARCHAR(255) NOT NULL, -- Company name
    industry VARCHAR(50) CHECK (industry IN (
        'HedgeFund', 'QuantTrading', 'AssetManagement', 'InvestmentBank',
        'CommercialBank', 'FinancialServices', 'Insurance', 'FinancialAdvisor',
        'Fintech', 'Technology', 'Exchange', 'Consulting', 'PensionFund', 'Etc'
    )), -- Industry category
    importance INTEGER CHECK (importance IN (1, 2, 99)) DEFAULT 99, -- Importance rating
    headquarter VARCHAR(100), -- Headquarter location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Created date
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last updated date
    updated_by VARCHAR(100) -- Last editor
);

-- Create the positions table to store job position postings
CREATE TABLE positions (
    pztid VARCHAR(50) PRIMARY KEY, -- Unique position ID
    cpid VARCHAR(50) REFERENCES companies(cpid) ON DELETE CASCADE, -- Foreign key to companies table
    pztname VARCHAR(255) NOT NULL, -- Position title
    pztlevel VARCHAR(20) CHECK (pztlevel IN ('Intern', 'NewGrad', 'Associate', 'Senior', 'VP')), -- Position level
    year INTEGER NOT NULL, -- Posting year
    url TEXT, -- URL to job description
    jd TEXT, -- Full job description
    note TEXT, -- Additional notes
    recent BOOLEAN DEFAULT FALSE, -- True if created within last 7 days
    active BOOLEAN DEFAULT TRUE, -- True if still recruiting this year
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Created timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last updated timestamp
    updated_by VARCHAR(100), -- Last editor
    oa_first BOOLEAN DEFAULT FALSE -- Whether this user is first to review OA
);

-- Create the applied table to track which users have applied to which positions
CREATE TABLE applied (
    usrid VARCHAR(50) REFERENCES users(usrid) ON DELETE CASCADE, -- Foreign key to users
    pztid VARCHAR(50) REFERENCES positions(pztid) ON DELETE CASCADE, -- Foreign key to positions
    applied BOOLEAN DEFAULT FALSE, -- Whether the user applied
    applied_at TIMESTAMP, -- Timestamp of application
    PRIMARY KEY (usrid, pztid) -- Composite key
);
