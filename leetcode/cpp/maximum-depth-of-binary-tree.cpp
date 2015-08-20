// https://leetcode.com/problems/maximum-depth-of-binary-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) { return 0; }
        return std::max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

/*
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) { return 0; }

        int depth = 0;
        queue<TreeNode*> lst;

        lst.push(root);
        while (!lst.empty()) {
            depth++;
            int s = lst.size();

            for (int i = 0; i < s; i++) {
                TreeNode *leaf = lst.front();
                lst.pop();

                if (leaf->left) {
                    lst.push(leaf->left);
                }

                if (leaf->right) {
                    lst.push(leaf->right);
                }
            }
        }

        return depth;
    }
};
*/

/*
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) { return 0; }

        int depth = 0;
        queue<std::pair<TreeNode*, int>> lst;

        lst.push(std::make_pair(root, 0));
        while (!lst.empty()) {
            std::pair<TreeNode*, int> curr = lst.front();
            lst.pop();

            TreeNode *leaf = curr.first;
            int lvl = curr.second;

            if (leaf) {
                lst.push(std::make_pair(leaf->left, lvl + 1));
                lst.push(std::make_pair(leaf->right, lvl + 1));
                continue;
            }

            depth = max(depth, lvl);
        }

        return depth;
    }
};
*/
